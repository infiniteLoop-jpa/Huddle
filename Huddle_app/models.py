from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)  # Note: In practice, use a more secure way to store passwords (e.g., Django's built-in password hashing)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    people_assigned = models.TextField()  # Assuming a comma-separated list of people assigned
    deadline = models.DateField()

    def __str__(self):
        return self.name
    
class HuddleGroup(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Account, related_name='huddle_groups')
    # Add other fields as needed

    def __str__(self):
        return self.name