from django.contrib import admin
from mainapp import models


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email_id', 'phone', 'branch')
    list_display_links = ('id', 'user', 'name', 'email_id', 'phone', 'branch')
    search_fields = ('id', 'name')
    list_per_page = 20

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'title', 'ctc', 'location', 'mailto')
    list_display_links = ('id', 'company', 'title', 'ctc', 'location', 'mailto')
    search_fields = ('id', 'company', 'location')
    list_per_page = 20

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 20


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Job, JobAdmin)
admin.site.register(models.Event, EventAdmin)