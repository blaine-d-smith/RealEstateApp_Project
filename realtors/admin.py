from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'start_date_only')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name',)
    list_per_page = 20

    def full_name(self, obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    def start_date_only(self, obj):
        return obj.start_date.strftime('%B %d %Y')


admin.site.register(Realtor, RealtorAdmin)