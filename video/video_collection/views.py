from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from django.contrib import messages

def home(request):
    app_name = 'goblin banking'
    return render(request, 'video_collection/home.html',{'app_name':app_name})
def add(request):
    if request.method == 'Post':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                return redirect('video_list')
            except ValidationError:
                messages.warning(request, 'url is not good')
            except IntegeryError:
                messages.warning(request, ' this not a true url')

                messages.warning(request,'warning this is not a good request')
            return render(request,'video_collection/add.html', {'new_video_form':new_video_form})

    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form':new_video_form})

def video_playlist(request):
    videos = Video.objects.order.by('name')
    return render(request, 'video_collection/video_playlist' , {'videos':videos})
# Create your views here.
