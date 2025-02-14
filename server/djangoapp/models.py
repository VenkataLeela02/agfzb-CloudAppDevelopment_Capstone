from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Porsche')
    car_description = models.CharField(max_length=500)
    
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.car_description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='Porsche')
    dealer_id = models.IntegerField()
    SEDAN = 'SN'
    SUV = 'SV'
    WAGON = 'WG'
    CHOICE_OF_CARS = [
        (SEDAN,'Sedan'),
        (SUV,'SUV'),
        (WAGON,'Wagon')
    ]
    choice_of_cars = models.CharField(max_length=2,choices=CHOICE_OF_CARS, default=SEDAN)
    year = models.DateField()


    def __str__(self):
        return "Car Model" + self.name + "," + \
        "Dealer ID: " + self.dealer_id + "," + \
        "Choice of car: " + self.choice_of_cars + "," + \
        "Year:" + self.year


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview(models.Model):
    dealership = models.IntegerField(default=15)
    name = models.CharField(max_length=255, default='Berkly Shepley')
    review = models.CharField(max_length=255, default='Total grid-enabled service-desk')
    purchase = models.CharField(max_length=255, default=True)
    purchase_date = models.CharField(max_length=255, default='07/11/2020')
    car_make = models.CharField(max_length=255,default='Audi')
    car_model = models.CharField(max_length=255, default= 'A6')
    car_year = models.CharField(max_length=255,default='2010')
    id = models.IntegerField(primary_key=True)

    def __init__(self, dealership, name, review, purchase, purchase_date, car_make, car_model, car_year, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.id = id
        self.review = review
        self.purchase_date = purchase_date

    def __str__(self):
        return '%s %s %i %s %s %s %i %s %s' % (self.name, self.dealership, self.id, self.purchase, self.car_make,
        self.car_model, self.car_year, self.review, self.purchase_date) 
        
        
    