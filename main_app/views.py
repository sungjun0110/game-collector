from django.shortcuts import render
from django.http import HttpResponse

class Game:
    def __init__(self, title, description, rating):
        self.title = title
        self.description = description
        self.rating = rating

games = [
    Game('The Legend of Zelda: Breath of the Wild', 'Open World', 100),
    Game('World of Warcraft', 'MMORPG', 85),
    Game('Skyrim', 'RPG', 90)
]

# Create your views here.
def home(request):
    return render(request, 'games/index.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', { 'games': games })