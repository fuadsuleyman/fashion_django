from django.db import models
# import birthday

from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):

    CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )

    # informations
    first_name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Surname', max_length=40)
    username = models.CharField('Username', max_length=50)
    email = models.EmailField("Email", max_length=254)
    password = models.CharField(max_length=50)
    gender = models.PositiveIntegerField(("Gender"), choices=CHOICES)
    address = models.CharField("Address", max_length=256)
    image = models.ImageField("Image", upload_to='users_images')

    birthday = models.DateTimeField()
    # objects = birthday.managers.BirthdayManager()

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.first_name}'

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=200, null=True, blank=True)
    email = models.CharField('Email', max_length=200, null=True, blank=True)
    device = models.CharField('Device', max_length=200, null=True, blank=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ('created_at',)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)