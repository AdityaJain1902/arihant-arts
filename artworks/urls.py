from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.collection, name='collection'),
    path('enquiry/<int:art_id>/', views.create_enquiry, name='create_enquiry'),
]



