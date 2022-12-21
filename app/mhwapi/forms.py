from django import forms
from .models import User, Monsters

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()
        
class MonsterForm(forms.ModelForm):
    class Meta:
        model = Monsters
        exclude = ()