from django.shortcuts import render
from .models import *
# Create your views here.


def portfilio_page(request , CIN):
    portfilio = Portfolio.objects.get(CIN=CIN)
    testimonials = Testimonial.objects.filter(portfolio=portfilio)
    if portfilio.gender == 'male':
        template = 'portfilio.html'
    elif portfilio.gender == 'female':
        template = 'portfilio_girls.html'
    
    context = {
        'portfilio': portfilio ,
        'testimonials' :testimonials
    }
    return render(request , template , context)