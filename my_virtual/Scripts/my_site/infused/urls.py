"""Определяет схемы URL для Infused."""
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'infused'
urlpatterns = [
    # Домашняя страница.
    path('', views.index, name='index'),
    # Страница со списком каналов.
    path('channels/', views.channels, name='channels'),
    # Страница с подробной информацией по отдельному каналу.
    path('channels/<int:channel_id>/', views.channel, name='channel'),
    # Страница для добавления нового канала.
    path('new_channel/', views.new_channel, name='new_channel'),
    # Страница для добавления новой записи.
    path('new_entry/<int:channel_id>/', views.new_entry, name='new_entry'),
    # Страница для добавления комментария пользователя.
    path('new_comments/<int:channel_id>', views.new_comments,
         name='new_comments'),
    # Страница для добавления видео.
    path('new_video/<int:channel_id>/', views.new_video, name='new_video'),
    # Страница для редактирования записей.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Страница для поиска.
    path('search_channel', views.search_channel, name='search_channel'),
]
