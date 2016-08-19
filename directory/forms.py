from django import forms

class CustomerSearchForm(forms.Form):
    customer_name = forms.CharField(label= 'Customer Name', min_length=0, max_length=30, required = False)
    sales_order = forms.CharField(label='Sales Order', min_length=0, max_length=30, required = False)

    def clean(self):
        if len(self.cleaned_data.get('customer_name')) == 0 and len(self.cleaned_data.get('sales_order')) == 0:
            raise forms.ValidationError("Must specify search criteria")
        return self.cleaned_data
