from django.contrib import admin
from .models import Channel, Entry, Video, Comments

admin.site.register(Channel)
admin.site.register(Entry)
admin.site.register(Video)
admin.site.register(Comments)
