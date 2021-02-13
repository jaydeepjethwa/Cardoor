from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CarAdmin(UserAdmin):
    list_display = ("carModel", "carNumber", "rate")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Car)
