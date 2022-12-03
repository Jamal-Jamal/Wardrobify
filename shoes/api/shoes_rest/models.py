from django.db import models
from django.urls import reverse


class Bin(models.Model):
    """
    The Bin model describes the name, size and number of the bin.
    """
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveIntegerField()
    bin_href = models.CharField(max_length=200, unique=True, null=True)

    class Meta:
        ordering = ("closet_name", "bin_number", "bin_size", "bin_href")


class Shoe(models.Model):
    """
    The Shoe model describes the manufactuering details: name, color, picture and bin where it exists.
    """

    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True)
    bin = models.ForeignKey(
        Bin,
        on_delete=models.CASCADE,
        related_name='shoes',
        null=True,
    )

    def get_api_url(self):
        return reverse("", kwargs={"show_bin": self.pk})

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ("manufacturer",)  # Default ordering for Shoes

    