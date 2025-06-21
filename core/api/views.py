from rest_framework.generics import (
     CreateAPIView,ListAPIView,UpdateAPIView,
    RetrieveAPIView,DestroyAPIView
    ,
)
from core.models import (
    Banner, Category, Form, About, Preference, Service,
    Mission, Mark, Product, CustomUser, Basket, Setting
)
from core.api.serializers import (
    BannerSerializer, CategorySerializer, FormSerializer, AboutSerializer,
    PreferenceSerializer, ServiceSerializer, MissionSerializer, MarkSerializer,
    ProductSerializer, CustomUserSerializer, BasketSerializer, SettingSerializer
)

# BANNER 
class BannerCreateView(CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerListView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerRetrieveView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerUpdateView(UpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDestroyView(DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer



# CATEGORY 
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




#  FORM 
class FormCreateView(CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormListView(ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormRetrieveView(RetrieveAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormUpdateView(UpdateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormDestroyView(DestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer



# ABOUT 
class AboutCreateView(CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutListView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutRetrieveView(RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutUpdateView(UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutDestroyView(DestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



# PREFERENCE
class PreferenceCreateView(CreateAPIView):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class PreferenceListView(ListAPIView):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class PreferenceRetrieveView(RetrieveAPIView):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class PreferenceUpdateView(UpdateAPIView):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

class PreferenceDestroyView(DestroyAPIView):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer







#SERVICE 
class ServiceCreateView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceUpdateView(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDestroyView(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

#Mission

class MissionCreateView(CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionListView(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionRetrieveView(RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionUpdateView(UpdateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionDestroyView(DestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


#Mark

class MarkCreateView(CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class MarkListView(ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class MarkRetrieveView(RetrieveAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class MarkUpdateView(UpdateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class MarkDestroyView(DestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


#Product

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#CustomUser

class CustomUserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserRetrieveView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDestroyView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



#Basket

class BasketCreateView(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class BasketListView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class BasketRetrieveView(RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class BasketUpdateView(UpdateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class BasketDestroyView(DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer




#Setting

class SettingCreateView(CreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingListView(ListAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingRetrieveView(RetrieveAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingUpdateView(UpdateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

class SettingDestroyView(DestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


