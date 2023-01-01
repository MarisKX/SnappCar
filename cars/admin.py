from django.contrib import admin
from .models import Car, MaintenceData


class MaintenceDataAdmin(admin.TabularInline):
    model = MaintenceData
    readonly_fields = ()
    list_display = (
        'car',
        'oil_change',
        'distribution_set',
    )


class CarAdmin(admin.ModelAdmin):
    inlines = (MaintenceDataAdmin, )
    readonly_fields = ()
    list_display = (
        'numberplate',
        'make',
        'model',
        'year',
        'fuel',
        'purchase_date',
        'sales_date',
        'residual_value',
    )

    ordering = ('numberplate',)


admin.site.register(Car, CarAdmin)
