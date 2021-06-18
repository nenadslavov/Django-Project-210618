from django.db import models
from django.urls import reverse


class Kategorija(models.Model):
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('naziv',)
        verbose_name = 'kategorija'
        verbose_name_plural = 'kategorije'

    def __str__(self): return self.naziv

    def ApsolutniURL(self): return reverse(
        'ProdavnicaPloca:ListaPlocaPoKategoriji', args=[self.slug])


class Ploca(models.Model):
    kategorija = models.ForeignKey(
        Kategorija, related_name='ploce', on_delete=models.CASCADE)
    album = models.CharField(
        max_length=200, db_index=True, default='album')
    autor = models.CharField(max_length=200, db_index=False)
    slug = models.SlugField(max_length=200, db_index=True)
    slika = models.ImageField(upload_to='ploce/%Y/%m/%d', blank=True)
    pesme = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=3)
    na_stanju = models.BooleanField(default=True)
    kreirana = models.DateTimeField(auto_now_add=True)
    azurirana = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('album',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'ploce'

    def __str__(self): return self.album

    def ApsolutniURL(self): return reverse(
        'ProdavnicaPloca:DetaljiPloca', args=[self.id, self.slug])
