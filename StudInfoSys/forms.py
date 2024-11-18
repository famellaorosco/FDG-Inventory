from django import forms
from .models import Supplier
from .models import FacilityInventory,InventoryItem
from django.forms import inlineformset_factory


class SupplierForm(forms.ModelForm):
    class Meta:

        model = Supplier
        fields = [
            'sname', 'item', 'phone_prefix', 'contact_number', 
            'contact_email', 'status', 'contact_person', 
            'address', 'zip_code', 'barangay_number'
        ]
        widgets = {
            'sname': forms.TextInput(attrs={'id': 'supplierName'}),
            'item': forms.Select(attrs={'id': 'item'}, choices=[('Item1', 'Item1'), ('Item2', 'Item2')]),  # Add item choices
            'phone_prefix': forms.Select(attrs={'id': 'phonePrefix'}, choices=[('+63', '+63'), ('+1', '+1')]),  # Add phone prefixes
            'contact_number': forms.TextInput(attrs={'id': 'phoneNumber'}),
            'contact_email': forms.EmailInput(attrs={'id': 'emailAddress'}),
            'status': forms.Select(attrs={'id': 'status'}, choices=[('Active', 'Active'), ('Inactive', 'Inactive')]),
            'contact_person': forms.TextInput(attrs={'id': 'contactPerson'}),
            'address': forms.TextInput(attrs={'id': 'address'}),
            'zip_code': forms.TextInput(attrs={'id': 'zipCode'}),
            'barangay_number': forms.TextInput(attrs={'id': 'barangayNumber'}),
        }


#class for adding facility
class FacilityInventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply CSS classes to the form fields
        self.fields['facility'].widget.attrs.update({'class': 'form-select'})
        self.fields['room_number'].widget.attrs.update({'class': 'textinput form-control'})

    # Facility and room_number fields with choices and input field respectively
    facility = forms.ChoiceField(
        choices=[('Classroom', 'Classroom'), ('Office', 'Office'), ('Library', 'Library'), ('Clinic', 'Clinic')],
        required=True
    )
    room_number = forms.CharField(max_length=50, required=True)

    class Meta:
        model = FacilityInventory
        fields = ['facility', 'room_number']


#class for adding stock in facility(this is inside formset)
class InventoryItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply CSS classes to the form fields
        self.fields['item_name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'value': 1, 'min': 1})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = InventoryItem
        fields = ['item_name', 'quantity', 'price']
        # No need to specify widgets here since we handle them in __init__()


# This will create a formset for the FacilityStockForm to allow multiple forms
InventoryItemFormSet = inlineformset_factory(FacilityInventory, InventoryItem, form=InventoryItemForm, extra=1)

