from django.contrib import admin

from .models import FormHourly, FormDaily2, FormMonthly


# Register your models here.
admin.site.register(FormHourly)
admin.site.register(FormDaily2)
admin.site.register(FormMonthly)
