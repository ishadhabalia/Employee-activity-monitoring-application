from django.contrib import admin
from .models import UserBuffer, UserBufferLocation, UserBufferData

# Register your models here.
admin.site.register(UserBuffer)
admin.site.register(UserBufferLocation)
admin.site.register(UserBufferData)
