from django.db import models
from django.urls import reverse


class BinVO(models.Model):
    """
    The Bin model describes the name, size and number of the bin.
    """
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveIntegerField()
    import_href = models.CharField(max_length=200, unique=True, null=True)


class Shoe(models.Model):
    """
    The Shoe model describes the manufactuering details: name, color, picture and bin where it exists.
    """

    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True, blank=True)
    bin = models.ForeignKey(
        BinVO,
        related_name='bins',
        on_delete=models.CASCADE,
        null=True
    )

    def get_api_url(self):
        return reverse("show_shoe", kwargs={"pk": self.pk})

    def __str__(self):
        return self.model_name
