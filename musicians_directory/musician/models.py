from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.CharField(max_length=20, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.IntegerField(verbose_name="Phone Number")
    instrument_type = models.CharField(max_length=20, verbose_name="Instrument Type")

    def __str__(self):
        return self.first_name