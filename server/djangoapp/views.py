from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .restapis import get_dealers_from_cf, get_dealer_by_state_from_cf, get_dealer_reviews_from_cf,post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import requests

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def get_about(request):
    context = {}
    if request.method == "GET":
        return render(request,'djangoapp/about.html', context)
    

# Create a `contact` view to return a static contact page
def get_contact(request):
    context = {}
    if request.method == "GET":
        return render(request,'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/about.html', context)
    else:
        return render(request, 'djangoapp/about.html', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    logout(request)
    # Redirect user back to course list view
    return redirect('djangoapp:index')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # <HINT> Get user information from request.POST
        # <HINT> username, first_name, last_name, password
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['psw']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, password=password)
            # <HINT> Login the user and 
            # redirect to course list page
            login(request, user)
            return redirect("djangoapp:dealerdetails")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    url = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/dealerships/dealer-get"
        # Get dealers from the URL
        
    dealerships = get_dealers_from_cf(url)
        
    if request.method == "GET":
        
        
        # Concat all dealer's short name
        #dealer_names = ' , '.join([dealer.short_name for dealer in dealerships])
        context = {'dealerships' : dealerships }
        # Return a list of dealer short name
        #state = "CA"
        #url_state = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/dealerships/dealer-get?state="+state

        #dealerships_by_state = get_dealer_by_state_from_cf(url, state=state)

        #dealer_names_by_state = ' , '.join([dealer.short_name for dealer in dealerships_by_state])
        
        
        #url_reviews = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/reviews" 

        #reviews = get_dealer_reviews_from_cf(url_reviews, dealerId=dealerId)

    return render(request, 'djangoapp/index.html', context)
    #return HttpResponse(dealerships)


# Create a `get_dealer_details` view to render the reviews of a dealer

def get_dealer_details(request, dealer_id):
    context = {}

    url = "https://1065db83.eu-gb.apigw.appdomain.cloud/api//reviews?id="+ str(dealer_id)

    reviews = get_dealer_reviews_from_cf(url, dealer_id=dealer_id)

    url_for_dealers = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/dealerships/dealer-get?id=" + str(dealer_id)

    dealers = get_dealers_from_cf(url_for_dealers, dealer_id = dealer_id)

    if request.method == "GET":
           
        context = {'reviews' : reviews,
        "dealers" : dealers }

        #reviewsList = ' , '.join([review.review for review in reviews])

    return render(request, 'djangoapp/dealer_details.html', context)

        #return HttpResponse(reviews)





# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

def add_review(request, dealer_id):
    if request.method == "GET":
        url = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/reviews?id=" + str(dealer_id)

        reviews = get_dealer_reviews_from_cf(url, dealer_id=dealer_id)

        url_for_dealers = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/dealerships/dealer-get?id=" + str(dealer_id)

        dealer_by_id = get_dealers_from_cf(url_for_dealers, dealer_id = dealer_id)

        context = {'reviews' : reviews,
        "dealers" : dealer_by_id }

        #reviewsList = ' , '.join([review.car_model for review in reviews])

        return render(request, 'djangoapp/add_review.html', context)
    
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        
            
            context = {}
            review = {
                "time" : datetime.utcnow().isoformat(),
                "dealership" : 1,
                "review" : "This is a great service",
                "name" : "name",
                "purchase" : 2020
            }

            json_payload = { "review" : review }
            
            #url_for_reviews = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/reviews?id=" + str(1)

            #reviews = get_dealer_reviews_from_cf(url_for_reviews, dealer_id=dealer_id)

            #url_for_dealers = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/dealerships/dealer-get?id=" + str(1)

            #dealer_by_id = get_dealers_from_cf(url_for_dealers, dealer_id = dealer_id)

            url = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/dealerships/dealer-get?id=" + str(dealer_id)  

            result = post_request(url, json_payload, dealer_id=dealer_id)
            
            url_for_reviews = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/reviews?id=" + str(dealer_id)

            reviews = get_dealer_reviews_from_cf(url_for_reviews, dealer_id=dealer_id)

            url_for_dealers = "https://1065db83.eu-gb.apigw.appdomain.cloud/api/dealerships/dealer-get?id=" + str(dealer_id)

            dealers = get_dealers_from_cf(url_for_dealers, dealer_id = dealer_id)

            context = { 'reviews' : reviews,
        "dealers" : dealers,
            "result" : result  }

    #return render(request, 'djangoapp/dealerdetails.html', context)
    return HttpResponse(result)
        











