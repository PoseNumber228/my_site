from django import forms

from .models import Channel, Entry, Video


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
