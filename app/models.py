from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django_countries.fields import CountryField

class Address(models.Model):
    street_address = models.CharField(max_length=300)
    apartment = models.CharField(max_length=255)
    town = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    telephone = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20)
    country = CountryField(blank_label='(select country)')

    def __str__(self):
        return f"Town: {self.town}, State: {self.state}"

class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    
class Volunteers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='volunteers')
    amount_contributed = models.PositiveIntegerField(default=0, blank=True,null=True)
    phone = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=100)
    service = models.TextField(max_length=150)
    reason_joined = models.TextField(max_length=150)
    address = models.ForeignKey(Address, blank=True, null=True, default='', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    approved = models.BooleanField(default=0)
    
    def __str__(self):
        return f"{self.user.username}, "
    

class Partners(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partners')
    amount_contributed = models.PositiveIntegerField(default=0, blank=True,null=True)
    phone = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=100)
    service = models.TextField(max_length=150)
    reason_joined = models.TextField(max_length=150)
    is_organisation = models.BooleanField(default=False)
    address = models.ForeignKey(Address, blank=True, null=True, default='', related_name='address', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    approved = models.BooleanField(default=0)
    
    def __str__(self):
        return self.user.username  

class Donors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donors')
    amount = models.PositiveIntegerField(default=0, blank=True,null=True)
    is_organisation = models.BooleanField(default=False)
    organisation = models.ForeignKey(Organization,blank=True, null=True, default='', related_name='organization', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=100)
    reason = models.TextField(max_length=150)
    address = models.ForeignKey(Address, blank=True, null=True, default='', related_name='addresss', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, default='')
    approved = models.BooleanField(default=0)
    
    def __str__(self):
        return self.user.username
    
    
    

    
  