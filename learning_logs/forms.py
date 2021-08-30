from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    # Here we define a class "TopicForm" which inherits from "forms.ModelForm"
    # This class consists of a nested Meta class telling Django which model to base the form on and what to include
    class Meta:
        model = Topic # Here we build a form from the 'Topic' model and include only the text field
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # The widget attribute is included in the above line.
        # Widget is an HTMl form element, and by specifying this, you can override default widgets of Django
        # By using "forms.Textarea" element, we're customizing the input widget for the field 'text' and then the text area wull be 80 columns wide

