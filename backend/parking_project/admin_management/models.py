from django.db import models
from django.contrib.auth.models import User
from parking_app import constants, choices
from core import models as core_model


class Plot(core_model.BaseModel):
    plot_id = models.CharField(verbose_name="Plot ID", max_length=40, unique=True)
    plot_name = models.CharField(verbose_name="Plot Name", max_length=40)
    city = models.CharField(verbose_name="City", max_length=40, null=True, blank=True)
    plot_address = models.CharField(verbose_name="Plot Address", max_length=300)

    def __str__(self):
        return f"{self.id}-{self.plot_id}-{self.plot_name}"
