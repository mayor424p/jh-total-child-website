from django.contrib import admin
from .models import AdmissionApplication

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'surname',
        'other_names',
        'gender',
        'proposed_year_of_entry',
        'father_phone',
        'mother_phone',
        'submitted_at',
    )

    list_filter = (
        'gender',
        'proposed_year_of_entry',
        'submitted_at',
    )

    search_fields = (
        'surname',
        'other_names',
        'father_phone',
        'mother_phone',
    )

    ordering = ('-submitted_at',)

    readonly_fields = ('submitted_at',)
