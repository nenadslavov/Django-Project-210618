from django.shortcuts import render, get_object_or_404
from KorpaZaKupovinu.forms import FormaZaDodavanjePloceUKorpu
from .models import Kategorija, Ploca
from KorpaZaKupovinu.korpa import Korpa


def ListaPloca(request, kategorija_slug=None):  # katalog je html odgovor
    kategorija = None
    kategorije = Kategorija.objects.all()
    ploce = Ploca.objects.filter(na_stanju=True)
    if kategorija_slug:
        kategorija = get_object_or_404(Kategorija, slug=kategorija_slug)
        ploce = ploce.filter(kategorija=kategorija)
        korpa = Korpa(request)
    else:
        kategorija = None
        ploce = None
        korpa = None
    return render(request, 'ProdavnicaPloca/ploca/list.html',
                  {'kategorija': kategorija, 'kategorije': kategorije,
                   'ploce': ploce, 'korpa': korpa})
# vraćanje podatka o automobilu prema id i slug kao html odgovor


def DetaljiPloca(request, id, slug):
    ploca = get_object_or_404(Ploca, id=id, slug=slug, na_stanju=True)
    korpa = Korpa(request)
    formazadodavanjeplocaukorpu = FormaZaDodavanjePloceUKorpu()
    return render(request, 'ProdavnicaPloca/Ploca/detail.html', {'ploca': ploca,
                                                                 'formazadodavanjeplocaukorpu': formazadodavanjeplocaukorpu,
                                                                 'korpa': korpa})
