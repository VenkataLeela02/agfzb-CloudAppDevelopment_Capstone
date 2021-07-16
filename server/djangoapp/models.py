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


# <HINT> Create a plain Python class `DealerReview` to hold review data
