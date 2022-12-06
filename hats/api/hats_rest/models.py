from django.db import models
from django.urls import reverse

class LocationVO(models.Model):
    closet_name = models.CharField(max_length=200)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()
    import_href = models.CharField(max_length=200)


    def get_api_url(self):
        return reverse("api_show_location", kwargs={"pk": self.pk})


class Hat(models.Model):
    fabric = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True, blank=True)

    location = models.ForeignKey(
        LocationVO,
        related_name="hats",
        null=True,
        on_delete=models.CASCADE,
    )
