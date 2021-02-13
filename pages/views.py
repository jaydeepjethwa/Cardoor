from django.shortcuts import render, HttpResponse


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


def faq(request):
    return render(request, 'faq.html')