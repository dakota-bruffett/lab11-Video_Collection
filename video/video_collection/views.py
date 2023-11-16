from django.shortcuts import render

def home(request):
    app_name = 'goblin banking'
    return render(request, 'video_collection/home.html',{'app_name':app_name})

# Create your views here.
