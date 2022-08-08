from django.db import models

class Business(models.Model):
    name_business = models.CharField(max_length=255)
    """Service Categories"""
    service_categories = models.ManyToManyField(
        'test_run_migrate.ServiceCategory', 
        related_name='service_categories_business',
        null=True, 
        default=None
    )
    is_active = models.BooleanField(default=False)




class ServiceCategory(models.Model):
    name_service_category = models.CharField(max_length=255)

class Service(models.Model):
    name_service = models.CharField(max_length=255)
    category = models.ForeignKey("test_run_migrate.ServiceCategory", on_delete=models.CASCADE, related_name="category_services")
    amount = models.IntegerField(default=1)

class ServiceBusiness(models.Model): 

    service = models.ForeignKey(
        'test_run_migrate.Service', 
        on_delete=models.CASCADE, related_name='service_businesses'
    )

    business = models.ForeignKey(
        'test_run_migrate.Business', 
        on_delete=models.CASCADE, 
        related_name='business_services'
    )
    