from django.contrib import admin

from .models import Participant

admin.site.disable_action('delete_selected')
admin.site.site_header = 'Future of Thai NLP Registration'
admin.site.site_title = 'Future of Thai NLP Registration'
admin.site.index_title = 'Future of Thai NLP Registration'

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'organization', 'email', 'is_checked_in']
    search_fields = ['full_name', 'organization', 'email']
    ordering = ['full_name']
