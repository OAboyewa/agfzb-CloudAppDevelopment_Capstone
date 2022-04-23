from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=30)

    # Create a toString method for object string representation
    def __str__(self):
        return self.name + " " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SPORTS = 'Sports'
    SEDAN = 'Sedan'
    WAGON = 'Wagon'
    SUV = 'Suv'
    COUPE = 'Coupe'

    carChoices = [
        (SPORTS, 'Sports'),
        (SEDAN, 'Sedan'),
        (WAGON, 'Wagon'), 
        (SUV, 'Suv'), 
        (COUPE, 'Coupe')
    ]

    car_make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    id = models.IntegerField(default=0, primary_key=True)
    car_model = models.CharField(null=False, max_length=30, choices=carChoices)
    car_year = models.DateField(null=False)

    # Create a toString method for object string representation
    def __str__(self):
        return str(self.car_make) + " " + self.name + " " + str(self.id) + " " + self.car_model +  " " +  str(self.car_year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
