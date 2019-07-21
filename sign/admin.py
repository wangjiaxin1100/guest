from django.contrib import admin
from sign.models import Event,Guest
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    search_fields = ['name']
    list_filter = ['status']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','crate_time','event']
    search_fields = ['raalname','phone']
    list_filter = ['sign']
admin.site.register(Event)
admin.site.register(Guest)