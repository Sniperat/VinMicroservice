from django.contrib import admin
from .models import DetailModel, WeightModel


class StackInlineWeight(admin.StackedInline):
    model = WeightModel
    # fields = ['file']
    extra = 0


class DetailAdmin(admin.ModelAdmin):
    list_display = ('vin_id', 'year', 'make','model','color','_type')
    list_filter = ('vin_id', 'year', 'make','model','color','_type')
    search_fields = ('vin_id', 'year','model')
    inlines = [StackInlineWeight]
    

admin.site.register(DetailModel, DetailAdmin)
admin.site.register(WeightModel)
