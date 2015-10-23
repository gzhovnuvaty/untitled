from datetime import datetime, timedelta, date
from django import forms
import floppyforms as forms



class ContactForm(forms.Form):
    lat_from = forms.IntegerField()
    lon_from = forms.IntegerField()
    lat_to = forms.IntegerField()
    lon_to = forms.IntegerField()
    people = forms.IntegerField(initial=2, min_value=1, max_value=8)
    user_id = forms.IntegerField(initial=17)
    date = forms.DateField(initial=datetime.now)
    time = forms.TimeField(initial= lambda :(datetime.today() + timedelta(hours=1)))

    def get_current_time(self):
        return datetime.now()

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message