from distutils.log import Log
import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Game, Release, Photo
from .forms import PlayhistoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'games/index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    releases_game_doesnt_have = Release.objects.exclude(id__in = game.releases.all().values_list('id'))
    playhistory_form = PlayhistoryForm()
    return render(request, 'games/detail.html', { 
            'game': game, 'playhistory_form': playhistory_form,
            'releases': releases_game_doesnt_have
        })

@login_required
def add_playhistory(request, game_id):
    # create a ModelForm instance using the data in request.POST
    form = PlayhistoryForm(request.POST)
    # validate the form
    if form.is_valid():
        new_playhistory = form.save(commit=False)
        new_playhistory.game_id = game_id
        new_playhistory.save()
    return redirect('detail', game_id=game_id)

@login_required
def assoc_release(request, game_id, release_id):
    Game.objects.get(id=game_id).releases.add(release_id)
    return redirect('detail', game_id=game_id)

@login_required
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            print(url)
            Photo.objects.create(url=url, game_id=game_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'genre', 'rating']
    
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)



class GameUpdate(UpdateView):
    model = Game
    fields = ['genre', 'rating']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'

class ReleaseList(LoginRequiredMixin, ListView):
    model = Release

class ReleaseDetail(LoginRequiredMixin, DetailView):
    model = Release

class ReleaseCreate(LoginRequiredMixin, CreateView):
    model = Release
    fields = '__all__'

class ReleaseUpdate(LoginRequiredMixin, UpdateView):
    model = Release
    fields = ['platform']

class ReleaseDelete(LoginRequiredMixin, DeleteView):
    model = Release
    success_url = '/releases/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)