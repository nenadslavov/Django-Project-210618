from decimal import Decimal
from django.conf import settings
from ProdavnicaPloca.models import Ploca


class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)

        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}
            self.korpa = korpa

    def __iter__(self):  # za view i sablone
        ploce_ids = self.korpa.keys()
        ploce = Ploca.objects.filter(id__in=ploce_ids)
        korpakopija = self.korpa.copy()
        for ploca in ploce:
            korpakopija[str(ploca.id)]['ploca'] = ploca
        for stavka in korpakopija.values():
            stavka['cena'] = Decimal(stavka['cena'])
            stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
            yield stavka  # vraca generator

    def __len__(self):  # za ukupan broj plocaa u korpi
        return sum(stavka['kolicina'] for stavka in self.korpa.values())

    def Dodaj(self, ploca, kolicina=1, dodati_na_kolicinu=True):
        ploca_id = str(ploca.id)
        if ploca_id not in self.korpa:
            self.korpa[ploca_id] = {'kolicina': 0, 'cena': str(ploca.cena)}
        if dodati_na_kolicinu:
            self.korpa[ploca_id]['kolicina'] += kolicina
        else:
            self.korpa[ploca_id]['kolicina'] = kolicina
        self.sesija.modified = True

    def Ukloni(self, ploca):
        ploca_id = str(ploca.id)
        if ploca_id in self.korpa:
            del self.korpa[ploca_id]
            self.sesija.modified = True

    def ObrisiJeIzSesije(self):
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in
                   self.korpa.values())
