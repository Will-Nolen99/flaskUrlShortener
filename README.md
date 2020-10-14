# flaskUrlShortener
URL shortener implemented in python using flask

# How to use
Run main.py to start the webserver.
The console provides the address to the server.

# Functionality
The application is a simple web app that allows users to enter URLs to be shortened.

The enterend URL is then stored in a sqlalchemy database and given a unique id.

The app returns a url directing to a specific page of the web app. 

That page then redircts to its corresponding website.

In the URL modifier entry box the use is able to modify the resulting shortened URL to have custom text in the shortened url.

The modifier will always be put infront of the unique URL id.
