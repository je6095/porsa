from django.shortcuts import render
from .forms import CustomerSearchForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CustomerSearchForm(request.POST)
    else:
        form = CustomerSearchForm()

    return render(request, 'calendar/event_month_list', {'form':form})

def customer_search(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('calendar/event_month_list'))
    form = CustomerSearchForm(request.POST)

    if form.is_valid():
        return HttpResponseRedirect(reverse('calendar/event_month_list'))

    customer_name = ""
    sales_order = ""

    if form.cleaned_data.get('customer_name') != None:
        c_prefix = form.cleaned_data.get('customer_name')
    if form.cleaned_data.get('sales_order') != None:
        s_prefix = form.cleaned_data.get('sales_order')

    matches = User.objects.filter(customer_start = c_prefix, sales_start = s_prefix)
    return render(request, 'calendar/results.html', {'results' : matches})
