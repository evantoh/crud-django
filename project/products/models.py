from django.db import models

class product(models.Model):
    description=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2,max_digits=9)
    quantity=models.IntegerField()

    def __str__(self):
        return self.description

