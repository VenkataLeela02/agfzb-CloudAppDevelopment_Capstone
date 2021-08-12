from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel, DealerReview

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealer_id')
    list_filter = ('year', 'choice_of_cars')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ('name', 'description')


# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(DealerReview)