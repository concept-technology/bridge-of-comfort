from django.shortcuts import render, redirect
from .forms import DonorForm

# Create your views here.
def home_view(request):
    return render(request, 'app/index.html')

    
def about_view(request):
    return render(request, 'app/about.html')

from django.shortcuts import render, redirect
from .forms import DonorForm, AddressForm
from .models import Address

def donor_create_view(request):
    if request.method == 'POST':
        donor_form = DonorForm(request.POST)
        address_form = AddressForm(request.POST)

        if request.POST.get('address_choice') == 'new' and address_form.is_valid():
            address = address_form.save()
            if donor_form.is_valid():
                donor = donor_form.save(commit=False)
                donor.user = request.user
                donor.address = address
                donor.save()
                return redirect('success_page')
        elif donor_form.is_valid():
            donor = donor_form.save(commit=False)
            donor.user = request.user
            donor.save()
            return redirect('success_page')

    else:
        donor_form = DonorForm()
        address_form = AddressForm()

    return render(request, 'app/donate.html', {
        'donor_form': donor_form,
        'address_form': address_form,
    })
