from django.contrib import admin
from mycmdb.models import Host

class HostAdmin(admin.ModelAdmin):
    list_display = ("hostname", "ip", "cpu", "mem", "disk", 'desc')

admin.site.register(Host, HostAdmin)
