from django.db import models

class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    attributes = models.ManyToManyField(Attribute, blank=True)

    def __str__(self):
        return self.name

class ContactFormPage(models.Model):
    title = models.CharField(max_length=100)
    schema = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.title
