from django import views
from django.shortcuts import render


class Home(views.View):
    def get(self, request):
        return render(request, 'home.html', {})
