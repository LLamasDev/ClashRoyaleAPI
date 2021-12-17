from django.db import models

class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    alias = models.CharField(max_length=45)
    tag = models.CharField(max_length=12)
    idioma = models.CharField(max_length=9)
    usoTotal = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'usuario'
        ordering = ('-usoTotal',)

    def __str__(self) -> str:
        return self.alias