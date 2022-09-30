from django.db import models

class about(models.Model):
    CATEGORIA_CHOICES = (
        ('gra','Graduação'),
        ('pos','Pós-graduação'),
        ('vol','Trabalhos voluntários'),
        ('cer','Certificações'),
        ('cur','Cursos')
    )

    name = models.CharField(max_length=150)
    link = models.CharField(max_length=1500)
    category = models.CharField(max_length=3, choices=CATEGORIA_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.name