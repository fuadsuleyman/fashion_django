from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    phone_num = models.CharField('Phone Number', max_length=50, null=True)
    email = models.EmailField('Email', max_length=50)
    message = models.TextField('Message', null=True)

    # moderations
    status = models.BooleanField('status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_message'
        verbose_name = 'Contact_Message'
        verbose_name_plural = 'Contact_Messages'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'