from django.contrib import admin, messages

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



class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name = "dure"
    title = "Duration"


    def lookups(self, request, model_admin):
        return(
            ('1 Month', 'Less than 1 month'),
            ('3 Months', 'Less than 3 months'),
            ('+3 Months', 'More than 3 months')
        )

    def queryset(self, request, queryset):
        if self.value() == "1 Month":
            return queryset.filter(dure__lte=30)
        if self.value() == "3 Months":
            return queryset.filter(dure__gt=30, dure__lte=90)
        if self.value() == "+3 Months":
            return queryset.filter(dure__gt=90)

def set_Valid(modeladmin, request, queryset):
    rows = queryset.update(isValid=True)
    if rows == 1:
        msg = "1 projet was"
    else:
        msg = f"{rows} project were"
    messages.success(request, message =f"{rows} successfully marked as valid")
set_Valid.short_description = "Validate"


def set_InValid(modeladmin, request, queryset):

    aux = queryset.filter(isValid=False)
    if aux.count() > 0:
        messages.error(request, "Projects already set to InValid")
    else :
        rows = queryset.update(isValid=False)
        if rows == 1:
            msg = "1 projet was"
        else:
            msg = f"{rows} project were"
        messages.success(request, message =f"{rows} successfully marked Non Valid")
set_InValid.short_description = "InValidate"


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    #actions = [set_Nonvalid]
    #actions = [set_Valid]
    actions_on_bottom = True
    actions_on_top = True
    actions = [set_Valid, set_InValid]

    list_filter = (
        'creator',
        'isValid',
        ProjectDurationFilter
    )

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

    #radio_fields = {'supervisor': admin.VERTICAL}
    autocomplete_fields = ['supervisor']
    empty_value_display = '-empty-'

admin.site.register(Student, StudentAdmin)
# admin.site.register(Coach,CoachAdmin) // when u write down @admin.register(Coach) it replaces this line
# admin.site.register(Projet)
