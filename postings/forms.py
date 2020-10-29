from django import forms
from .models import ProjectPost

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectPost
        fields = ['title', 'description', 'image']