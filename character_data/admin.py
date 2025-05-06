from django.contrib import admin
from .models import Character

# Register your models here.
class CharacterAdmin(admin.ModelAdmin):
  list_display = ("fullname","gender","specificRole")
  
admin.site.register(Character,CharacterAdmin)
