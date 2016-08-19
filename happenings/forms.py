from django import forms
from django.forms import ModelForm
from .models import Event
from django.db import models
from django.utils import timezone
import sys

class EventForm(ModelForm):
    def clean_start_onlydate(self):
        if(self.data['start_onlydate'] == ""):
            raise forms.ValidationError("Enter valid start date.")
        else:
            return self.cleaned_data['start_onlydate']

    def clean_start_onlytime(self):
        if(self.data['start_onlytime'] == ""):
            raise forms.ValidationError("Enter valid start time.")
        else:
            return self.cleaned_data['start_onlytime']

    def clean_end_onlydate(self):
        if(self.data['end_onlydate'] == ""):
            raise froms.ValidationError("Enter valid end date.")
        else:
             return self.cleaned_data['end_onlydate']

    def clean_end_onlytime(self):
        if(self.data['end_onlytime'] == ""):
            raise froms.ValidationError("Enter valid end time.")
        else:
            return self.cleaned_data['end_onlytime']

    def clean_start_date(self):
        data = timezone.now()
        if self.data['start_onlydate'] == "" or self.data['start_onlytime'] == "":
            if(self.data['start_onlydate'] == ""):
                raise forms.ValidationError("Enter valid start date.")
            if(self.data['start_onlytime'] == ""):
                raise forms.ValidationError("Enter valid start time.")
        else:
            print("Warning: ", self.data['start_onlydate'], file=sys.stderr)
            print("Warning: ", self.data['start_onlytime'], file=sys.stderr)
            myDate = self.cleaned_data['start_onlydate']
            myTime = self.cleaned_data['start_onlytime']
            data = data.replace(year=myDate.year)
            data = data.replace(month=myDate.month)
            data = data.replace(day=myDate.day)
            data = data.replace(hour=myTime.hour)
            data = data.replace(minute=myTime.minute)
            data = data.replace(second=myTime.second)
        return data

    def clean_end_date(self):
        data = timezone.now()
        if self.data['end_onlydate'] == "" or self.data['end_onlytime'] == "":
            if(self.data['start_onlydate'] == ""):
                raise forms.ValidationError("Enter valid end date.")
            if(self.data['start_onlytime'] == ""):
                raise forms.ValidationError("Enter valid end time.")
        else:
            print("Warning: ", self.data['end_onlydate'], file=sys.stderr)
            myDate = self.cleaned_data['end_onlydate']
            myTime = self.cleaned_data['end_onlytime']
            data = data.replace(year=myDate.year)
            data = data.replace(month=myDate.month)
            data = data.replace(day=myDate.day)
            data = data.replace(hour=myTime.hour)
            data = data.replace(minute=myTime.minute)
            data = data.replace(second=myTime.second)
        return data
    
    class Meta:
        model = Event
        fields =['title', 'start_onlytime', 'end_onlytime', 'start_onlydate', 'end_onlydate', 'start_date', 'end_date', 'description', 'phone', 'address_1', 'address_2', 'city', 'state', 'zipcode', 'sales_order', 'pick', 'weight', 'pallet', 'driver']
        widgets = {
            'start_onlytime' : forms.TimeInput(attrs={'type':'time'}),
            'end_onlytime' : forms.TimeInput(attrs={'type':'time'}),
            'start_onlydate' : forms.DateInput(attrs={'type':'date'}),
            'end_onlydate' : forms.DateInput(attrs={'type':'date'})
        }
