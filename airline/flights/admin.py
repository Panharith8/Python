from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import Flight,Airport,Passenger


# Register your models here.
class FlgihtAdmin(admin.ModelAdmin):
    list_display=("id","origin", "destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)


admin.site.register(Airport)
admin.site.register(Flight, FlgihtAdmin)
admin.site.register(Passenger,PassengerAdmin)


