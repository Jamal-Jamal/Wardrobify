from django.db import models
from django.urls import reverse

class LocationVO(models.Model):
    closet_name = models.CharField(max_length=200)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()
    import_href = models.CharField(max_length=200)

    # def __str__(self):
    #     return f"(self.closet_name) - {self.section_number}/{self.shelf_number}"

    # class Meta:
    #     ordering = ("closet_name", "section_number", "shelf_number")


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

    # def get_api_url(self):
    #     return reverse("api_show_hats", kwargs={"id": self.id})

    # def __str__(self):
    #     return self.style
