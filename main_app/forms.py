from django.forms import ModelForm
from .models import Playhistory

class PlayhistoryForm(ModelForm):
    class Meta:
        model = Playhistory
        fields = ['date', 'playtime']