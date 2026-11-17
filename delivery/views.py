from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("   Welcome to the Delivery App! This is the home page.")

def thanku(request):
    return HttpResponse("Thank you for your order! Your order has been placed successfully.")