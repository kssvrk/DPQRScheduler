from django.contrib import admin
from jobs.models import Script,Jobs


class JobsAdmin(admin.ModelAdmin):
    exclude = ('started_at','finished_at','created_at','status','result_description')

# Register your models here.
admin.site.register(Script)
admin.site.register(Jobs,JobsAdmin)