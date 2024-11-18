from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    sname = models.CharField(max_length=255)  # Supplier Name
    item = models.CharField(max_length=255)  # Selected Item
    phone_prefix = models.CharField(max_length=5, blank=True, null=True)  # Phone Prefix
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # Phone Number
    contact_email = models.EmailField(max_length=255, blank=True, null=True)  # Email Address
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])  # Status
    contact_person = models.CharField(max_length=255)  # Contact Person
    address = models.TextField(blank=True, null=True)  # Address (Optional)
    zip_code = models.CharField(max_length=10, blank=True, null=True)  # ZIP Code (Optional)
    barangay_number = models.CharField(max_length=10, blank=True, null=True)  # Barangay Code (Optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return self.sname


#add facility stock 
class FacilityInventory(models.Model):
    FACILITY_CHOICES = [
        ('Classroom', 'Classroom'),
        ('Office', 'Office'),
        ('Library', 'Library'),
        ('Clinic', 'Clinic'),
    ]
    
    id = models.AutoField(primary_key=True)
    facility = models.CharField(max_length=100, choices=FACILITY_CHOICES)
    room_number = models.CharField(max_length=20)
    date_added = models.DateField(auto_now_add=True)

class InventoryItem(models.Model):
    inventory = models.ForeignKey(FacilityInventory, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
