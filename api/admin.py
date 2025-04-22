from django.contrib import admin
from api.models import Group, Personne

class GroupeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created', 'date_updated')

class personneAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_updated')

admin.site.register(Group, GroupeAdmin)
admin.site.register(Personne, personneAdmin)
