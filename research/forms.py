from dataclasses import fields
from django.forms import ModelForm
from .models import Research


class ResearchForm(ModelForm):
    class Meta:
        model = Research
        fields = ['research_title', 'body', 'source', 'tags' ]