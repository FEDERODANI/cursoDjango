from django.db import models


class Producto(models.Model):
	nombre = models.CharField(max_length=250)
	precio = models.DecimalField(max_digits=9, decimal_places=2)
	cantidad = models.IntegerField(default=0)

	# Si esta en True significa que esta activo
	activo = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to="productos", null=True, blank=True)

	class Meta:
		db_table="productos"

	def __str__(self):
		return f"[{self.id}] {self.nombre}"
