from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ProdavnicaPloca.models import Ploca
from .korpa import Korpa
from .forms import FormaZaDodavanjePloceUKorpu


@require_POST
def DodajUKorpu(request, ploca_id):
    korpa = Korpa(request)
    ploca = get_object_or_404(Ploca, id=ploca_id)
    form = FormaZaDodavanjePloceUKorpu(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(ploca=ploca,
                    kolicina=cd['kolicina'],
                    dodati_na_kolicinu=cd['dodati_na_kolicinu'])
    return redirect('KorpaZaKupovinu:DetaljiKorpe')


@require_POST
def UkloniIzKorpe(request, automobil_id):
    korpa = Korpa(request)
    ploca = get_object_or_404(Ploca, id=automobil_id)
    korpa.Ukloni(ploca)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')


def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjePloceUKorpu(
            initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    return render(request, 'KorpaZaKupovinu/detail.html', {'korpa': korpa})
