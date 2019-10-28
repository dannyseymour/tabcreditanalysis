## Tab Credit Analysis REST API

A lightweight REST API currently built with Django and intended for deployment on Heroku.
The goal is to migrate to Gunicorn to handle HTTP requests more efficiently.

This API takes calls either from the Android app directly, or through the Tab Java Servlet, and performs
calculations to return a credit score based on several factors. The algorithm is a work in progress.