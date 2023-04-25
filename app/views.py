from django.shortcuts import render, redirect
from .forms import DetailsForm, yearForm
from .models import Details
from django.db.models import Count
from django.db.models import Q
import math

def add_details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)

        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page
            return redirect('/')
    else:
        # Show a blank form
        form = DetailsForm()

    return render(request, 'add_details.html', {'form': form})


def show_charts(request):
    global year
    if request.method == 'POST':
        yform = yearForm(request.POST)
        year = yform['year'].value()
    else:
        yform = yearForm()
        year = 2023

    tcount = len(Details.objects.filter(year=year).values())

    #placed / not placed info
    placed_ct = len(Details.objects.filter(year=year, placed = True).values())
    not_placed_ct = len(Details.objects.filter(year=year, placed = False).values())
    
    placed_pt = calcPerc(placed_ct, placed_ct+not_placed_ct)
    not_placed_pt = calcPerc(not_placed_ct, placed_ct+not_placed_ct)

    #core / it info
    core_ct = len(Details.objects.filter(year=year, placed_on = "core").values())
    it_ct = len(Details.objects.filter(year=year, placed_on = "IT(software)").values())
    
    core_pt = calcPerc(core_ct, core_ct+it_ct)
    it_pt = calcPerc(it_ct, core_ct+it_ct)

    #salary
    l26 = len(Details.objects.filter(year=year, package = "2-6").values())
    l612 = len(Details.objects.filter(year=year, package ="7-12").values())
    l128 = len(Details.objects.filter(year=year, package = "13-18").values())
    l184 = len(Details.objects.filter(year=year, package ="19-24").values())
    l24 = len(Details.objects.filter(year=year, package ="more").values())
    salTotal = l26+l128+l184+l612+l24

    l26pt = calcPerc(l26, salTotal)
    l612pt = calcPerc(l612, salTotal) + l26pt
    l128pt = calcPerc(l128, salTotal) + l612pt
    l184pt = calcPerc(l184, salTotal) + l128pt
    l24pt = calcPerc(l24, salTotal) + l184pt

    sdata = {
        "l26":l26, "l26pt":l26pt,
        "l612":l612, "l612pt": l612pt,
        "l128":l128, "l128pt": l128pt,
        "l184": l184, "l184pt": l184pt,
        "l24":l24, "l24pt":l24pt
    }

    data = {"pc":placed_ct, "npc":not_placed_ct, "pt": placed_pt, "npt":not_placed_pt, "tot":tcount, "cc":core_ct, "ic":it_ct, "ct": core_pt, "it": it_pt}

    return render(request, 'charts.html', {"data":data, "sdata": sdata, "form":yform})

def calcPerc (v, tot):
    return math.floor((((v/tot)*100)/100)*360)