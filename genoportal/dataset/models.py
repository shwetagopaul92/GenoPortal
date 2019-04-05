from django.db import models


# To create a model for storing datasets
class Dataset(models.Model):
    filename = models.CharField(max_length=64, default="")
    file = models.FileField(upload_to='dataset/datasetfiles')

    def __str__(self):
        return f"{self.filename}"


# To allow users to upload datasets
class UploadDataset(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='dataset/datasetfiles')

    class Meta:
        db_table = "upload"


# To allow users to post a contact form
class ContactForm(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    emailaddress = models.CharField(max_length=64)
    querytype = models.CharField(max_length=64)
    message = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} |  {self.querytype}"
