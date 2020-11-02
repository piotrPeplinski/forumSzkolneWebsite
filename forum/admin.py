from django.contrib import admin
from forum.models import Question


class DateField(admin.ModelAdmin):
    readonly_fields = ('createDate',)


admin.site.register(Question, DateField)
