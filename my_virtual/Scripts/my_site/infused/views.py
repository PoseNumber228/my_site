from django.shortcuts import render, redirect
from .models import Channel, Video, Entry
from .forms import ChannelForm, EntryForm, VideoForm, CommentsForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Домашняя странца приложения Infused"""
    return render(request, 'infused/index.html')


def channels(request):
    """Выводит список каналов."""
    channels = Channel.objects.order_by('date_added')
    context = {'channels': channels}
    return render(request, 'infused/channels.html', context)


@login_required()
def video(request, channel_id):
    """Выводит список видео"""
    videos = Video.objects.get(id=channel_id)
    context = {"video": videos}
    return render(request, "infused/channels.html", context)


def channel(request, channel_id):
    """Выводит одну тему и все её записи."""
    channel = Channel.objects.get(id=channel_id)
    entries = channel.entry_set.order_by('-date_added')
    comments = channel.comments_set.order_by('date_added')
    videos = channel.video_set.order_by('-date_added')
    context = {'channel': channel, 'entries': entries, 'video': videos,
               'comments': comments}
    return render(request, 'infused/channel.html', context)


@login_required()
def new_channel(request):
    """Определяет новый канал."""
    if request.method != 'POST':
        # Данные не отправлялись; создаётся пустая форма.
        form = ChannelForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = ChannelForm(data=request.POST)
        if form.is_valid():
            new_channel = form.save(commit=False)
            new_channel.owner = request.user
            new_channel.save()
            return redirect('infused:channels')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'infused/new_channel.html', context)


def new_comments(request, channel_id):
    """Добавлет комметарий к конкретной записи."""
    channel = Channel.objects.get(id=channel_id)
    if request.method != 'POST':
        form = CommentsForm()
    else:
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            new_comments = form.save(commit=False)
            new_comments.channel = channel
            new_comments.save()
            return redirect('infused:channel', channel_id=channel_id)

    context = {'channel': channel, 'form': form}
    return render(request, 'infused/new_comments.html', context)


@login_required()
def new_entry(request, channel_id):
    """Добавляет запись по конкретной теме."""
    channel = Channel.objects.get(id=channel_id)
    if channel.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Данные не отправлялись; создаётся пустая форма.
        form = EntryForm()
    else:
        # Отправленны данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.channel = channel
            new_entry.save()
            return redirect('infused:channel', channel_id=channel_id)

    # Вывести пустую или недействительную форму.
    context = {'channel': channel, 'form': form}
    return render(request, 'infused/new_entry.html', context)


@login_required()
def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    channel = entry.channel
    if channel.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправленны данные POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('infused:channel', channel_id=channel.id)

    # Вывести пустую или недействительную форму.
    context = {'entry': entry, 'channel': channel, 'form': form}
    return render(request, 'infused/edit_entry.html', context)


@login_required()
def new_video(request, channel_id):
    """Добавляет запись по конкретной теме."""
    channel = Channel.objects.get(id=channel_id)
    if channel.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Данные не отправлялись; создаётся пустая форма.
        form = VideoForm()
    else:
        # Отправленны данные POST; обработать данные.
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.channel = channel
            new_video.save()
            return redirect('infused:channel', channel_id=channel_id)

    # Вывести пустую или недействительную форму.
    context = {'channel': channel, 'form': form}
    return render(request, 'infused/new_video.html', context)


def search_channel(request):
    if request.method == "POST":
        searched = request.POST['searched']
        channels = Channel.objects.filter(text__contains=searched)
        context = {'searched': searched, 'channels': channels}
        return render(request, 'infused/search_channel.html', context)
    else:
        context = {}
        return render(request, 'infused/search_channel.html', context)
