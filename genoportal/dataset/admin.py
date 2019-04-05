from django.contrib import admin
from dataset import models

# Register your models here.
admin.site.register(models.Dataset)
admin.site.register(models.UploadDataset)
admin.site.register(models.ContactForm)
