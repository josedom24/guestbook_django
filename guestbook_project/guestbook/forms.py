from django import forms

class EntryForm(forms.Form):
    info = forms.CharField(label="", max_length=255, required=True, widget=forms.TextInput(attrs={
        "id": "guestbook-entry-content",
        "autocomplete": "off"
    }))
