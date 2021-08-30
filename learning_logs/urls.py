"""Defines URL patterns for learnign_logs"""

from django.urls import path, include
from . import views

app_name = "learning_logs"

urlpatterns = [
    # It contains the list of individual pages that can be requested from the learning_logs app
    # Home page
    path('', views.index, name = 'index'),
    # Page that will show all the topics
    path('topics/', views.topics, name = 'topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name = 'new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry')
    # An actual URL pattern is a call to the path function which takes in three arguments:
    # '' -> it matches the base URL. It is used to return the URL properly
    # "views.index" specifies which function to call in views.py
    # name = "index" specifies the name for the URL pattern so we can refer to it in other code sections
    # We can use the name for referring to the home page rather than writing out the URL
]

