from django.contrib import admin
from .models import Game, Playhistory, Release, Photo

# Register your models here.
admin.site.register(Game)
admin.site.register(Playhistory)
admin.site.register(Release)
admin.site.register(Photo)