
import random

from django.shortcuts import render, get_object_or_404

from .models import Mineral


def mineral_list(request):
    ''' create the list view of the mineral '''
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'minerals/index.html',
                  {'minerals': minerals, 'random_mineral' : random_mineral})
                                 
def mineral_detail(request, pk):
    ''' create the detail view of a single mineral '''
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html',
                  {'mineral' : mineral, 'random_mineral' : random_mineral})
