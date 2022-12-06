from django.db import models

class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveIntegerField()
    import_href = models.CharField(max_length=200)


class Shoe(models.Model):
    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField(null=True, blank=True)
    bin = models.ForeignKey(
        BinVO,
        related_name='shoes',
        on_delete=models.PROTECT,
    )
