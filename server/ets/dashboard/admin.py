from django.contrib import admin
from dashboard.models import UserBuffer, UserBufferLocation, UserBufferData
# Register your models here.
@admin.register(UserBuffer)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name']
    class Meta:
        model = UserBuffer

@admin.register(UserBufferLocation)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['user_id']
    class Meta:
        model = UserBufferLocation
        
@admin.register(UserBufferData)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'process_name']
    class Meta:
        model = UserBufferData