from django import forms


class ContactForm(forms.Form):
    lat_from = forms.CharField(max_length=9)
    lon_from = forms.CharField(max_length=9)
    lat_to = forms.CharField(max_length=9)
    lon_to = forms.CharField(max_length=9)
    people = forms.IntegerField()
    data = forms.DateTimeField()
    time = forms.TimeField()



    def clean_message(self):
            message = self.cleaned_data['message']
            num_words = len(message.split())
            if num_words < 4:
                raise forms.ValidationError("Not enough words!")
            return message