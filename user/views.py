from django.shortcuts import render, redirect, get_object_or_404

from .forms import TrCreationForm
from .models import TigerReserve, State

# Create your views here.

#Views to add Tiger Reserves
def tr_home(request):
    return render(request, 'users/tr_home.html')

def tr_add(request):
    return render(request, 'users/tr_add.html')

# def tr_create_view(request):
#     form = TrCreationForm()
#     if request.method == 'POST':
#         form = TrCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('tr_add')
#     return render(request, 'users/tr_add.html', {form: 'form'})


# def tr_update_view(request, pk):
#     TigerReserve = get_object_or_404(TigerReserve, pk=pk)
#     form = TrCreationForm(instance=TigerReserve)
#     if request.method == 'POST':
#         form = TrCreationForm(request.POST, instance=TigerReserve)
#         if form.is_valid():
#             form.save()
#             return redirect()

#     return 
