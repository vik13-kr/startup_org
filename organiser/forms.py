from django import forms 
from django.core.exceptions import ValidationError

from .models import Newslink, Startup, Tag

class SlugCleanMixin:
    '''mixin class for slug cleaning'''
    def clean_slug(self) :
        new_slug = (self.cleaned_data['slug'].lower()) 
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create". ')
        return new_slug

class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()

class NewsLinkForm(SlugCleanMixin, forms.ModelForm):
    #we don't have any name cleaning method because we dont need to validate the name of the newslinks.
    class Meta:
        model = Newslink
        fields = '__all__'


class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'