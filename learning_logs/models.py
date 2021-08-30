from django.db import models
from django.contrib.auth.models import User

# You can create your models from here

class Topic(models.Model):
    # Model is a parent class included in Django that defines a model's basic functionality
    """A topic the user is learning about"""
    # "text" and "date_added" are the two attributes of the class Topic
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    # "auto_now_add = True" sets this attribute to current date and time whenever we create a new topic
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    # After adding owner field to the Topic, it establishes a foreign key relationship to the User model
    # If a user is deleted, all the topics associated with the user are also deleted


    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learnt about a topic"""

    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    # ForeignKey is a reference to another record in database
    # on_delete = models.CASCADE tells Django that when a topic is deleted, all entries associated with that topic should be deleted as well
    # This is called as Cascading delete
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        # Here, we nested Meta class under Entry class for holding extra information for managing the model
        # We set a special attribute telling Django to use "Entries" when it needs to refer to more than one entry
        # If we don't set it to "entries", Django would refer to multiple entries as "entrys"
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""

        return f"{self.text[:50]}..."
        # Here, we just show the first 50 characters.. of the entry