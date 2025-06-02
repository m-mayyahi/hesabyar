from django.shortcuts import *
from .models import hesabketab
from .forms import hesabketabform

def add_hesabketab(request):
    if request.method == "POST":
        form= hesabketabform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hesabketab_list')
    else:
        form = hesabketabform()
        
    return render(request, 'hesab/add_hesabketab.html', {'form': form})
def hesabketab_list(request):
    Hesabketab = hesabketab.objects.all().order_by('-date')
    return render(request, 'hesab/hesabketab_list.html',{'hesabketab': Hesabketab})