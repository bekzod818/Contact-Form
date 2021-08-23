from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'theme']
    list_display_links = ['name', 'theme']
