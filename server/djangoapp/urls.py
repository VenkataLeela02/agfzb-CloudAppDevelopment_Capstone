from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    #path(route='', view=views.)
    # path for about view
    path(route='about/', view=views.get_about, name='about'),

    # path for contact us view
    path(route='contact/', view=views.get_contact, name='contact'),
    # path for registration
    path('registration/', view=views.registration_request, name='registration'),
    # path for login
  

    # path for logout
    path(route='contact/', view=views.logout_request, name='contact'),

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealerdetails'),
    # path for add a review view
    path('addreview/<int:dealer_id>/', views.add_review, name='addreview'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)