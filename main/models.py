from django.db import models


# (django.contrib.postgres.fields.JSONField is removed except for support in historical migrations
# from django.contrib.postgres.fields import JSONField


class DetailModel(models.Model):
    vin_id = models.CharField(max_length=17, primary_key=True)
    year = models.CharField(max_length=4, null=True)
    make = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=True)

    # I have no idea what's 'type'
    _type = models.SmallIntegerField(choices=(
        (0, 'type1'),
        (1, 'type2')
    ), default=0, verbose_name='type_for_what')

    color = models.CharField(max_length=255, null=True)
    dimensions = models.JSONField(null=True)


class WeightModel(models.Model):
    detail = models.ForeignKey(DetailModel,
                               related_name=("weight"),
                               on_delete=models.CASCADE)
    _type = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)
    value = models.IntegerField()
