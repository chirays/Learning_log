from django.contrib import admin

# Register your models here.

from .models import Topic, Entry
# The "." here tells Django to look for models.py in the same directory as the admin.py


admin.site.register(Topic)
admin.site.register(Entry)
