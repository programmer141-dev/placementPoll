from django.urls import path
from . import views
urlpatterns=[
    path('',views.add_details,name='add_details'),
  
]