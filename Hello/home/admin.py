from django.contrib import admin
from home.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    list_display_links = ('id','name')
    
    
admin.site.register(Contact,ContactAdmin)