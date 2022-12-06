from django.db import models
from django.urls import reverse


class Location(models.Model):
    closet_name = models.CharField(max_length=100)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()

    def get_api_url(self):
        return reverse("api_location", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.closet_name} - {self.section_number}/{self.shelf_number}"

    class Meta:
        ordering = ("closet_name", "section_number", "shelf_number")


class Bin(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()

    def get_api_url(self):
        return reverse("api_bin", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.closet_name} - {self.bin_number}/{self.bin_size}"

    class Meta:
        ordering = ("closet_name", "bin_number", "bin_size")
