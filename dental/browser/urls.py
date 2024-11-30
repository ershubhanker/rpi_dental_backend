from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
        
    path('index/', index, name='index'),
    path('api/patients/', patient_list_create, name='patient_list_create'),
    path('api/patients/<int:pk>/', patient_detail, name='patient_detail'),
    path('api/patients/search/', patient_search, name='patient_search'),

]