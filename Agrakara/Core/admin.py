from django.contrib import admin

from .models import Temple

class TempleAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'contact_number', 'created_at')
    search_fields = ('name', 'district', 'pooja_timings')
    list_filter = ('district',)

admin.site.register(Temple, TempleAdmin)



