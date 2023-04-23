from django.shortcuts import render, redirect
from .forms import DetailsForm
from .models import Details
from django.db.models import Count
from django.db.models import Q

def add_details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)

        if form.is_valid():
            print(form)

            # Save the form data to the database
            form.save()
            # Redirect to a success page
            return redirect('/')
    else:
        # Show a blank form
        form = DetailsForm()

    return render(request, 'add_details.html', {'form': form})


