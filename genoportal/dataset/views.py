from django.shortcuts import render
from .models import Dataset
from .forms import UploadForm
from .models import UploadDataset
from .models import ContactForm
from django import forms
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse, FileResponse, HttpResponse


# To allow users to view the Products page
def products(request):
    return render(request, "dataset/products.html")


# To allow users to view the Contact Us page
def contactus(request):
    return render(request, "dataset/contactus.html")


# To allow users to view the Knowledge Center page
def knowledgecenter(request):
    return render(request, "dataset/knowledgecenter.html")


# To allow users to view the Dataset Details page
def datasetdetails(request):
    return render(request, "dataset/datasetdetails.html")


# To get the values from the ContactForm
def contactform(request):
    name = request.POST["name"]
    gender = request.POST["gender"]
    emailaddress = request.POST["emailaddress"]
    querytype = request.POST["querytype"]
    message = request.POST["message"]
    contact_new = ContactForm()
    contact_new.name = name
    contact_new.gender = gender
    contact_new.emailaddress = emailaddress
    contact_new.querytype = querytype
    contact_new.message = message
    contact_new.save()
    context = {
      "name": name,
      "querytype": querytype
    }
    return render(request, "dataset/formsubmitted.html", context)


# To render the dataset details for the website
def dataset(request):
    context = {
        "dataset": Dataset.objects.all(),
        "uploadeddataset": UploadDataset.objects.all()
    }
    return render(request, "dataset/datasetnames.html", context)


# To render the upload dataset page
def uploadform(request):
    return render(request, "dataset/uploadform.html")


# To get the entries of the dataset upload form
def uploaddataset(request):
    upload = False
    if request.method == "POST":
        MyUploadForm = UploadForm(request.POST, request.FILES)
        if MyUploadForm.is_valid():
            upload = UploadDataset()
            upload.name = MyUploadForm.cleaned_data["name"]
            upload.file = MyUploadForm.cleaned_data["file"]
            upload.save()
            upload = True
    else:
        MyUploadForm = UploadForm()
    return render(request, 'dataset/uploadsuccess.html', locals())


# To render the download dataset page
def downloaddataset(request):
    return render(request, "dataset/downloaddataset.html")


# To render the download dataset page
def download(request):
    datasetname = request.POST["name"]
    filepath = "datasetfiles/"
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % datasetname
    response['X-Sendfile'] = filepath
    return response


# To render the view dataset page
def viewdataset(request):
    datasetname = request.POST["name"]
    response = FileResponse(open('datasetfiles/%s'
                            % datasetname, 'rb'))
    return response


# To render the api view page
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api(request):
    queryset = Dataset.objects.all().values()
    return JsonResponse({"dataset details": list(queryset)})
