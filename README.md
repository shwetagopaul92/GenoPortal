# GenoPortal

An illustration of a Django App

The app uses Python, SQLite, HTML, CSS. 

Details : 

- I have created a web application called "GenoPortal" using Django and sqlite. The application is mobile responsive.

- In this app, users can register for a free trial. Once registered, they can log in to see what the platform has to offer. The GenoPortal platform offers genomic datasets that can be downloaded for free. I have uploaded some datasets using Django Admin interface. Users can also upload their own datasets to the app using a form and start using them. There is a products page, knowledge center page (scientific support), dataset details page allowing the user to understand how to use the platform. A page with the dataset names is given , allowing the users to search for the datasets they like, grab the name and download them if they wish to. 

I have also created an API view for a GET request, and accessing the app at /api allows users to view the datasets details. There is a contact form allowing users to post any queries to the support team, and once the form is submitted a message showing confirmation is shown. The details of the form are saved in the database. To integrate with S3, there is a link leading to Amazon S3 upload tutorial. 

- The dataset/datasetfiles has the .bed and .txt files required for this project. 


To use this App, 

1. Clone the github repository
2. cd genoportal/
3. python3 manage.py runserver



