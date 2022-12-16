from django import forms

from user.models import TigerReserve, Country, State

def TrCreationForm(request):
    class Meta:
        model = TigerReserve
        fields = '__all__'