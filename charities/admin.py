from django.contrib import admin

from charities.models import Task, Charity, Benefactor

admin.site.register(Task)
admin.site.register(Charity)
admin.site.register(Benefactor)

