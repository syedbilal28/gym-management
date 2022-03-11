from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="Index"),
    path("package/<int:package_id>/",views.PackagePrice,name="PackagePrice"),
    path("signup/",views.SignupMember,name="SignupMember"),
    path("search/<str:keyword>/",views.Search,name="Search")
]