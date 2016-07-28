from django.db import models

class Item(models.Model):
    # set up a text field
    text = models.TextField(default='')
