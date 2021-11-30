from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Profesor)
admin.site.register(models.Class)
admin.site.register(models.Student)
admin.site.register(models.Subject)
admin.site.register(models.Unit)
