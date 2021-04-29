from django.db import models

# Create your models here.
class Owners(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=300)
    age = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Owners"

class Dogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    owners = models.ForeignKey("Owners", on_delete=models.CASCADE, verbose_name = "owners")
    name = models.CharField(max_length=45)
    age = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Dog"

