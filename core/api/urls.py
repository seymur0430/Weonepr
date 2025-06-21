from django.urls import path
from .views import (
      # Banner
    BannerCreateView, BannerListView, BannerRetrieveView, BannerUpdateView, BannerDestroyView,
    # Category
    CategoryCreateView, CategoryListView, CategoryRetrieveView, CategoryUpdateView, CategoryDestroyView,
    # Form
    FormCreateView, FormListView, FormRetrieveView, FormUpdateView, FormDestroyView,
    # About
    AboutCreateView, AboutListView, AboutRetrieveView, AboutUpdateView, AboutDestroyView,
    # Preference
    PreferenceCreateView, PreferenceListView, PreferenceRetrieveView, PreferenceUpdateView, PreferenceDestroyView,
    # Service
    ServiceCreateView, ServiceListView, ServiceRetrieveView, ServiceUpdateView, ServiceDestroyView,
    # Mission
    MissionCreateView, MissionListView, MissionRetrieveView, MissionUpdateView, MissionDestroyView,
    # Mark
    MarkCreateView, MarkListView, MarkRetrieveView, MarkUpdateView, MarkDestroyView,
    # Product
    ProductCreateView, ProductListView, ProductRetrieveView, ProductUpdateView, ProductDestroyView,
    # Basket
    BasketCreateView, BasketListView, BasketRetrieveView, BasketUpdateView, BasketDestroyView,
    # Setting
    SettingCreateView, SettingListView, SettingRetrieveView, SettingUpdateView, SettingDestroyView,
    # CustomUser
    CustomUserCreateView, CustomUserListView, CustomUserRetrieveView, CustomUserUpdateView, CustomUserDestroyView,
)

urlpatterns = [
    # Banner
    path('banners/', BannerListView.as_view()),
    path('banners/create/', BannerCreateView.as_view()),
    path('banners/<int:id>/', BannerRetrieveView.as_view()),
    path('banners/<int:id>/update/', BannerUpdateView.as_view()),
    path('banners/<int:id>/delete/', BannerDestroyView.as_view()),

    # Category
    path('categories/', CategoryListView.as_view()),
    path('categories/create/', CategoryCreateView.as_view()),
    path('categories/<int:id>/', CategoryRetrieveView.as_view()),
    path('categories/<int:id>/update/', CategoryUpdateView.as_view()),
    path('categories/<int:id>/delete/', CategoryDestroyView.as_view()),

    # Form
    path('forms/', FormListView.as_view()),
    path('forms/create/', FormCreateView.as_view()),
    path('forms/<int:id>/', FormRetrieveView.as_view()),
    path('forms/<int:id>/update/', FormUpdateView.as_view()),
    path('forms/<int:id>/delete/', FormDestroyView.as_view()),

    # About
    path('about/', AboutListView.as_view()),
    path('about/create/', AboutCreateView.as_view()),
    path('about/<int:id>/', AboutRetrieveView.as_view()),
    path('about/<int:id>/update/', AboutUpdateView.as_view()),
    path('about/<int:id>/delete/', AboutDestroyView.as_view()),

    # Preference
    path('preferences/', PreferenceListView.as_view()),
    path('preferences/create/', PreferenceCreateView.as_view()),
    path('preferences/<int:id>/', PreferenceRetrieveView.as_view()),
    path('preferences/<int:id>/update/', PreferenceUpdateView.as_view()),
    path('preferences/<int:id>/delete/', PreferenceDestroyView.as_view()),

    # Service
    path('services/', ServiceListView.as_view()),
    path('services/create/', ServiceCreateView.as_view()),
    path('services/<int:id>/', ServiceRetrieveView.as_view()),
    path('services/<int:id>/update/', ServiceUpdateView.as_view()),
    path('services/<int:id>/delete/', ServiceDestroyView.as_view()),

    # Mission
    path('missions/', MissionListView.as_view()),
    path('missions/create/', MissionCreateView.as_view()),
    path('missions/<int:id>/', MissionRetrieveView.as_view()),
    path('missions/<int:id>/update/', MissionUpdateView.as_view()),
    path('missions/<int:id>/delete/', MissionDestroyView.as_view()),

    # Mark
    path('marks/', MarkListView.as_view()),
    path('marks/create/', MarkCreateView.as_view()),
    path('marks/<int:id>/', MarkRetrieveView.as_view()),
    path('marks/<int:id>/update/', MarkUpdateView.as_view()),
    path('marks/<int:id>/delete/', MarkDestroyView.as_view()),

    # Product
    path('products/', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('products/<int:id>/', ProductRetrieveView.as_view()),
    path('products/<int:id>/update/', ProductUpdateView.as_view()),
    path('products/<int:id>/delete/', ProductDestroyView.as_view()),

    # Basket
    path('baskets/', BasketListView.as_view()),
    path('baskets/create/', BasketCreateView.as_view()),
    path('baskets/<int:id>/', BasketRetrieveView.as_view()),
    path('baskets/<int:id>/update/', BasketUpdateView.as_view()),
    path('baskets/<int:id>/delete/', BasketDestroyView.as_view()),

    # Setting
    path('settings/', SettingListView.as_view()),
    path('settings/create/', SettingCreateView.as_view()),
    path('settings/<int:id>/', SettingRetrieveView.as_view()),
    path('settings/<int:id>/update/', SettingUpdateView.as_view()),
    path('settings/<int:id>/delete/', SettingDestroyView.as_view()),

    # CustomUser
    path('users/', CustomUserListView.as_view()),
    path('users/create/', CustomUserCreateView.as_view()),
    path('users/<int:id>/', CustomUserRetrieveView.as_view()),
    path('users/<int:id>/update/', CustomUserUpdateView.as_view()),
    path('users/<int:id>/delete/', CustomUserDestroyView.as_view()),
]