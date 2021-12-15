from django import forms
from django.core.validators import FileExtensionValidator

from .models import Channel, Entry, Video, Comments


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['text', 'video']
        labels = {'text': 'Video name:'}


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        labels = {'text': 'Comments:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
