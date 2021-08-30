from django.shortcuts import render, redirect
# render function renders the response based on the data provided by views
# redirect function takes in a name of a view and redirects the user to that view
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
# We have imported the model associated with the data we need
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


# Here, we are using the "login_required" decorator which checks whether the user is logged in
# and Django runs the code in topics() only if they are logged in
@login_required
def topics(request):
    # The paramter here is the "request" object Django received from the server
    """Show all the topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # Here, the query "Topic.objects.filter(owner=request.user)" tell Django to retrieve only the Topic objects from the database
    # whose owner attribute matches the current user
    # Also, we query the database by asking for the Topic objects by the data they are added
    context = {'topics': topics}  # Here we define the context that we will send to the template
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all it's entries"""
    topic = Topic.objects.get(id = topic_id)
    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added') # Here the "-" sign sorts the dates in reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data = request.POST)
        if form.is_valid():
            # When we first call form.save, we pass commit=False argument because we need to modify the new topic before saving it to the database
            new_topic = form.save(commit=False)
            # We then set the new topic's owner attribute to the current user attribute
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs: topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()

    else:
        # POST data submitted; process the data
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # we call "commit=False" to tell Django to create a new entry object and assign it to the new_entry without saving it to the database yet
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)

    # Display a blank or invalid form
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Editing an existing entry"""
    # Here we get the entry object, the user wants to edit and the topic associated with it
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill the form with existing entry
        form = EntryForm(instance = entry)

    else:
        # POST data submitted; process data
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            # We then redirect to the "topic" page where the user can see the updated version of the edited entry
            return redirect('learning_logs:topic', topic_id = topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)











