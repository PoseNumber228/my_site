from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    """Тема, которую изучает пользователь."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме."""
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возращает строковое представление модели."""
        if len(self.text[:50]) >= 50:
            return f"{self.text[:50]}..."
        else:
            return self.text


class Video(models.Model):
    """Видео, которое записывает пользователь."""
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4'])])

    class Meta:
        verbose_name_plural = 'videos'

    def __str__(self):
        """Возращает строкове представление модели."""
        return self.text
