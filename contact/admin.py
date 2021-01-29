from django.contrib import admin

# Register your models here.

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_num', 'email', 'created_at')
    list_display_links = ("first_name",)

admin.site.register(Contact, ContactAdmin)
