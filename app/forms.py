from django import forms
from .models import Donors, Address,Organization
from django_countries.widgets import CountrySelectWidget

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'country': CountrySelectWidget(attrs={'class': 'form-control'}),
            'street_address': forms.TextInput(attrs={'class': 'form-control'}),
            'apartment': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }




class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
        widgets = {
            'name': CountrySelectWidget(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donors
        exclude = ['user', 'created_at','is_organisation']
        # Keep other widgets as before

    class Meta:
        model = Donors
        exclude = ['user', 'created_at', 'approved']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'+234 000 0000 0000'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'reason_joined': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'is_organisation': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'id_is_organisation'}),
            'organisation': forms.Select(attrs={'class': 'form-control', 'id': 'id_organisation'}),
            'address': forms.Select(attrs={'class': 'form-control', 'id': 'id_existing_address'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control','placeholder':'how much are you donating?'}),
        }
        
        # def clean(self):
        #     cleaned_data = super().clean()
        #     is_individual = cleaned_data.get('is_individual')
        #     is_organisation = cleaned_data.get('is_organisation')
            

        #     if not is_individual and not is_organisation:
        #         raise forms.ValidationError("You must select either Individual or Organisation.")

        #     if is_individual and is_organisation:
        #         raise forms.ValidationError("You cannot select both Individual and Organisation.")

        #     return cleaned_data
