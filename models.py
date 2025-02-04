from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


# creating user model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def clean(self):
        if not self.username:
            raise ValidationError('Username is required')
        if not self.password:
            raise ValidationError('Password is required')
        if not self.email_id:
            raise ValidationError('Email ID is required')
        if not self.role:
            raise ValidationError('Role is required')

#creating products model
class Products(models.Model):
    CATEGORY_CHOICES = [
        ('TV_LCD', 'TV (LCD)'),
        ('TV_LED', 'TV (LED)'),
        ('TV_PLASMA', 'TV (PLASMA)'),
        ('TV_CRT', 'TV (CRT)'),
        ('AMPLIFIERS', 'Amplifiers'),
        ('SPEAKERS', 'Speakers'),
        ('PROJECTORS', 'Projectors'),
        ('MICROPHONE', 'Microphone'),
        ('MIXERS', 'Mixers'),
        ('TURN_TABLES', 'Turn Tables'),
        ('HEADPHONES', 'Headphones'),
        ('PC', 'PC'),
        ('SMART_DEVICE', 'Smart Device'),
        ('REMOTES', 'Remotes'),
        ('GAMING_CONSOLES', 'Gaming Consoles'),
    ]

    job_id = models.CharField(primary_key=True,max_length=100)
    prod_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.job_id 

    def clean(self):
        if not self.job_id:
            raise ValidationError('Job ID is required')
        if not self.prod_name:
            raise ValidationError('Product name is required')
        if not self.category:
            raise ValidationError('Category is required')
        if not self.brand:
            raise ValidationError('Brand is required')
        if not self.model:
            raise ValidationError('Model is required')
        if not self.description:
            raise ValidationError('Description is required')


#creating clients model
class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.EmailField(blank=True, null=True)
    phone_no = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    job_id = models.ForeignKey(Products, on_delete=models.CASCADE, db_column='job_id')

    def __str__(self):
        return str(self.client_id)

    def clean(self):
        if not self.first_name:
            raise ValidationError('First name is required')
        if not self.last_name:
            raise ValidationError('Last name is required')
        if not self.phone_no:
            raise ValidationError('Phone number is required')
        if not self.job_id:
            raise ValidationError('Job ID is required')

#creating Services model:
class Services(models.Model):
    PRIORITY_CHOICES = [
        ('URGENT', 'Urgent'),
        ('HIGH_PRIORITY', 'High Priority'),
        ('LOW_PRIORITY', 'Low Priority'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('GOING_ON', 'Going On'),
        ('FINISHED', 'Finished'),
        ('CANCELLED', 'Cancelled'),
    ]

    service_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE,db_column='client_id')
    job_id = models.ForeignKey(Products, on_delete=models.CASCADE, db_column='job_id')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    due_date = models.DateField()

    def __str__(self):
        return f"Service {self.service_id} for {self.client_id}"

    def clean(self):
        if not self.client_id:
            raise ValidationError('Client ID is required')
        if not self.job_id:
            raise ValidationError('Job ID is required')
        if not self.priority:
            raise ValidationError('Priority is required')
        if not self.status:
            raise ValidationError('Status is required')
        if not self.due_date:
            raise ValidationError('Due date is required')

#Creating Post_Services Model:
class PostServices(models.Model):
    job_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='post_services')
    user_description = models.TextField()
    work_hours = models.IntegerField()
    prod_name = models.CharField(max_length=255, blank=True)
    prod_description = models.TextField(blank=True)

    def __str__(self):
        return f"Post Service for {self.prod_name} (Job ID: {self.job_id.job_id})"

    def clean(self):
        if not self.job_id:
            raise ValidationError('Job ID is required')
        if not self.prod_description:
            raise ValidationError('Product description is required')
        if not self.work_hours:
            raise ValidationError('Work hours are required')

    def save(self, *args, **kwargs):
        # Populate prod_name and prod_description from the related Products record
        if not self.prod_name:
            self.prod_name = self.job_id.prod_name
        if not self.prod_description:
            self.prod_description = self.job_id.description
        super().save(*args, **kwargs)
