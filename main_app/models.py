from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

PLATFORMS = (
    # Windows
    ('W11', 'Windows 11'),
    ('W10', 'Windows 10'),
    ('W7', 'Windows 7'),
    # Mac
    ('M', 'Mac'),
    # Xbox
    ('XSX', 'XBox Series X'),
    ('XSS', 'XBox Series S'),
    ('XOS', 'XBox One S'),
    ('XOX', 'XBox One X'),
    ('XO', 'XBox One'),
    ('X36', 'XBox 360'),
    ('X', 'XBox'),
    # Playstations
    ('PS5', 'Playstation 5'),
    ('PS4', 'Playstation 4'),
    ('PS3', 'Playstation 3'),
    ('PS2', 'Playstation 2'),
    ('PS1', 'Playstation 1'),
    # Nintendo
    ('NS', 'Nintendo Switch'),
    ('WiU', 'Wii U'),
    ('Wii', 'Wii'),
    ('NGC', 'Nintendo GameCube'),
    ('N64', 'Nintendo 64'),
    # Mobile
    ('iOS', 'iOS'),
    ('And', 'Android'),
)

# Create your models here.
class Release(models.Model):
    platform = models.CharField(
        max_length=3,
        choices=PLATFORMS,
    )

    def __str__(self):
        return f"{self.get_platform_display()}"

    def get_absolute_url(self):
        return reverse('releases_detail', kwargs={'pk': self.id})

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.TextField(max_length=200)
    rating = models.IntegerField()
    releases = models.ManyToManyField(Release)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
class Playhistory(models.Model):
    date = models.DateField('Play Date')
    playtime = models.DecimalField(max_digits=3, decimal_places=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Played for {self.playtime} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"

        