from django.views import View 
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {'get_or_post': 'get'})

    def post(self, request):
        return render(request, 'home.html', {'get_or_post': 'post'})

