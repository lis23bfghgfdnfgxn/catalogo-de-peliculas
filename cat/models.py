from django.db import models
from base.models import ClaseModelo


########## GENERO ##########
class Genero(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del género',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def Save(self):
        self.descripcion = self.descripcion.upper()
        super(Genero, self).Save()

    class Meta:
        verbose_name_plural = 'Géneros'


########## SERIE ##########
class Serie(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la serie',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def Save(self):
        self.descripcion = self.descripcion.upper()
        super(Serie, self).Save()

    class Meta:
        verbose_name_plural = 'Series'


########## PELICULA ##########
class Pelicula(ClaseModelo):
    titulo = models.CharField(max_length=100,blank=False)
    sinopsis = models.TextField(max_length=500,blank=False)
    director = models.CharField(max_length=100,null=False,blank=True)
    fecha_estreno = models.DateField(null=True,blank=False)
    duracion = models.CharField(max_length=15,blank=False)
    imagen = models.ImageField(upload_to='cat/preview/',default='cat/preview/prew.png')
    url_video = models.CharField(max_length=250,null=False,blank=True)
    genero = models.ManyToManyField(Genero, blank = True)
    serie = models.ForeignKey(Serie, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.titulo)

    def save(self):
        self.titulo = self.titulo.upper()
        super(Pelicula,self).save()

    class Meta:
        verbose_name_plural = "Peliculas"
