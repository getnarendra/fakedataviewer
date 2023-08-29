from django import forms
from .models import MongoDBConnection

class MongoDBConnectionForm(forms.ModelForm):
    class Meta:
        model = MongoDBConnection
        fields = ['environment', 'host', 'port', 'username', 'password']
