from django.db import models
from django.contrib.auth.models import AbstractUser

class Banner(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to='banner_images/')
 
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return self.name
    

class Form(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(default=0)
    surname=models.CharField(max_length=100)
    note=models.TextField()

    def __str__(self):
        return self.name
    

class About(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to='about_images/')
    
    def __str__(self):
        return self.title
    

class Preference(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    icon=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.title
    

class Mission(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to='mission_images/')

    class Meta:
        ordering=('-id',)

    def __str__(self):
        return self.title
     

    
class Mark(models.Model):
    name=models.CharField(max_length=100)
    
    class Meta:
        ordering=('-id',)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    mark=models.ForeignKey(Mark,on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=60)
    mark=models.CharField(max_length=60)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='product_images/')
    image2=models.ImageField(upload_to='product_images/')

    class Meta:
        ordering=('-id',)

    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    PRICE_CHOICES = [
    ('sale', 'Satiş qiyməti'),
    ('discount', 'Endirimli qiymət'),
    ]
    adress=models.CharField(max_length=100)
    number=models.IntegerField(default=0)
    price_type =models.CharField(max_length=100,default='qiymeti daxil edin')
    
    def __str__(self):
        return self.adress
    

class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='basket')
    products = models.ManyToManyField(Product, related_name='wishlisted_by')
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.user
    

class Setting(models.Model):
    red_image=models.ImageField(upload_to='setting_images/')
    red_title=models.CharField(max_length=100)
    red_title=models.TextField()
    
    category_title=models.CharField(max_length=100)

    form_title=models.CharField(max_length=100)

    footer_content=models.TextField()
    footer_adress=models.CharField(max_length=100)
    footer_number=models.IntegerField(default=0)
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        # istəsən əlavə et: tiktok, github və s.
    ]
    
    social_media= models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=50)  # məsələn: 'fab fa-instagram'
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='social_links', null=True, blank=True)


    preference_title=models.CharField(max_length=100)


    activity_title=models.CharField(max_length=100)
    product_count=models.IntegerField(default=0)
    experience=models.IntegerField(default=0)
    sale_point=models.IntegerField(default=0)


    cooperation_title=models.CharField(max_length=100)
    cooperation_content=models.TextField()
    cooperation_image=models.ImageField(upload_to='setting_images/')
    

    service_title=models.CharField(max_length=100)
    service_content=models.TextField()
    

    mission_title=models.CharField(max_length=100)

    product_title=models.CharField(max_length=100)


    def __str__(self):
        return self.cooperation_content

