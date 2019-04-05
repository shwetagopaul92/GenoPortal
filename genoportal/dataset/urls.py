from django.urls import path

from . import views

urlpatterns = [
    path("dataset", views.dataset, name="dataset"),
    path("uploadform", views.uploadform, name="uploadform"),
    path("uploaddataset", views.uploaddataset, name="uploaddataset"),
    path("products", views.products, name="products"),
    path("knowledgecenter", views.knowledgecenter, name="knowledgecenter"),
    path("contactus", views.contactus, name="contactus"),
    path("contactform", views.contactform, name="contactform"),
    path("datasetdetails", views.datasetdetails, name="datasetdetails"),
    path("api", views.api, name="api"),
    path("download", views.download, name="download"),
    path("downloaddataset", views.downloaddataset, name="downloaddataset"),
    path("viewdataset", views.viewdataset, name="viewdataset")
]
