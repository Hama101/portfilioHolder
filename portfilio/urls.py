from django.urls import path , include
from . import views as v

urlpatterns = [
    path('portfilio/<str:CIN>/', v.portfilio_page, name='portfilio'),
]
