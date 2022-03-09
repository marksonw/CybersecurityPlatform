from dataclasses import fields
from django.forms import ModelForm, widgets
from .models import Research
from django import forms


class ResearchForm(ModelForm):
    class Meta:
        model = Research
        fields = ['banner_image','research_title', 'description', 'body', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    
    def __init__(self, *args, **kwargs):
        super(ResearchForm, self).__init__(*args, **kwargs)

        self.fields['tags'].widget.attrs.update({'class':'modtags'})