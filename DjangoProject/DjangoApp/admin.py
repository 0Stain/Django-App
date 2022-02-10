from django.contrib import admin
from .models import *


# Register your models here.

class ProjectInline(admin.StackedInline):
    model = Projet


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name'
    )
    fields = (
        ('first_name', 'last_name'),
        'email'
    )
    search_fields = ['last_name']
    inlines = [ProjectInline]


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name'
    )
    fields = (
        ('first_name', 'last_name'),
        'email'
    )
    search_fields = ['last_name']


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'dure',
        'temps_allocated',
        'besoin',
        'description',
        'isValid',
        'supervisor'
    )
    fieldsets = [
        (
            None,
            {
                'fields': ('isValid',)
            }
        ),
        (
            None,
            {
                'fields': (
                    'project_name',
                    ('creator', 'supervisor'),
                    'besoin',
                    'description',

                )
            }
        ),
        (
            'Durations',
            {
                'classes': ('collapse',),
                'fields': (
                    'dure',
                    'temps_allocated'
                )
            }
        )
    ]

    radio_fields = {'supervisor':admin.VERTICAL}

admin.site.register(Student, StudentAdmin)
# admin.site.register(Coach,CoachAdmin) // when u write down @admin.register(Coach) it replaces this line
# admin.site.register(Projet)
