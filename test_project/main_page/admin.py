from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from main_page.models import Slider


@admin.register(Slider)
class SorlableSliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['my_order']

# admin.site.register(Slider)
