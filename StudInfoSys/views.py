from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .forms import FacilityInventoryForm, InventoryItemFormSet
from .models import FacilityInventory,InventoryItem
from django.core.paginator import Paginator

def admin_homepage(request):
    return render(request, 'Admin_Home.html')

def add_inventory(request):
    if request.method == 'POST':
        facility_form = FacilityInventoryForm(request.POST)
        item_formset = InventoryItemFormSet(request.POST)

        if facility_form.is_valid() and item_formset.is_valid():
            facility_inventory = facility_form.save()  # Save the FacilityInventory instance
            item_formset.instance = facility_inventory
            item_formset.save()  # Save all InventoryItem instances under the same inventory ID
            return redirect('depart_inv')  # Redirect to list view

    else:
        facility_form = FacilityInventoryForm()
        item_formset = InventoryItemFormSet()

    return render(request, 'add_inv.html', {
        'facility_form': facility_form,
        'item_formset': item_formset,
    })


#function to display items
def facility_stock_list(request):
    # Filtering facilities based on GET parameters
    facility_filter = request.GET.get('facility', '')
    date_created_filter = request.GET.get('date_created', '')

    # Base query
    facilities = FacilityInventory.objects.prefetch_related('items').all()


    # Apply filters if specified
    if facility_filter:
        facilities = facilities.filter(facility=facility_filter)
    if date_created_filter:
        facilities = facilities.filter(date__date=date_created_filter)

    # Paginate results (if necessary)
    paginator = Paginator(facilities, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'inventory_items': facilities,  # Rename 'facilities' to 'inventory_items'
        'page_obj': page_obj,
        'facility_filter': facility_filter,
        'date_created_filter': date_created_filter,
    }
    return render(request, 'depart_inv.html', context)

# View to handle formset submission for a specific facility's stock
def update_facility_stock(request, facility_id):
    inventory_item = get_object_or_404(InventoryItem, id=facility_id)
    facility = inventory_item.inventory
    form = FacilityInventory(initial={'facility': facility.facility, 'room_number': facility.room_number})
    formset = InventoryItemFormSet(request.POST or None, queryset=InventoryItem.objects.filter(facility=facility.facility))

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()  # Saving the main facility info if any updates
            formset.save()  # Save stock items
            return redirect('update_stock_list', facility_id=facility.id)

    context = {
        'facility': facility,
        'form': form,
        'formset': formset,
    }
    return render(request, 'facility_stock_list.html', context)


def depreciated_inventory(request):
    return render(request, 'Depreciated_Inv.html')

def depart_inv(request):
    return render(request, 'Depart_Inv.html')

def purchase_request(request):
    return render(request, 'Purchase_Req.html')

def evaluation_request(request):
    return render(request, 'Eval_Req.html')

def add_supplier(request):
    return render(request, 'Add_Supplier.html')

def supplier_list(request):
    return render(request, 'Supplier_List.html')

def edit_supplier(request):
    return render(request, 'Edit_Supplier.html')

def equipment_maintenance(request):
    return render(request, 'Equip_Maintenance.html')

def add_purchase(request):
    return render(request, 'Add_Purch.html')