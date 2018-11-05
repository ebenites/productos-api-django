from django.db import models

# Create your models here.
class Producto (models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    imagen=models.FileField(upload_to='storage/images/', max_length=250, null=True)
    detalles=models.TextField(null=True)
    estado=models.BooleanField(default=1)
    
    class Meta:
        db_table = "productos"
        
    def __str__(self):
        return self.nombre