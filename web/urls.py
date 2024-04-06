from django.urls import path
from . import views
urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),
    path("contact/",views.contact,name='contact'),
    path('services/<str:slug>/', views.ServicesDetailView.as_view(), name='service_detail'),
    path('blog/<str:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
