from django.db import models


class DetailModel(models.Model):
    vin_id = models.CharField(max_length=17, primary_key=True)
    year = models.CharField(max_length=4, null=True)
    make = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=True)
    detail_type = models.PositiveSmallIntegerField(choices=(
        (0, 'type1'),
        (1, 'type2')
    ), default=0)

    color = models.CharField(max_length=255, null=True)
    dimensions = models.JSONField(null=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'


class WeightModel(models.Model):
    detail = models.ForeignKey(DetailModel,
                               related_name=("weight"),
                               on_delete=models.CASCADE)
    weight_type = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)
    value = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weights'
