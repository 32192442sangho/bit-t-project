from django.db import models
from ward_places.minimap_ward.models import MinimapWard


class MinOutput(models.Model):
    use_in_migration = True

    ward_place = models.AutoField(max_length=10, primary_key=True)
    x = models.IntegerField(max_length=10)
    y = models.IntegerField(max_length=10)

    minimap_ward = models.ForeignKey(MinimapWard, on_delete=models.CASCADE)

    class Meta:
        db_table = "min_output"

    def __str__(self):
        return f"{self.pk}, {self.x}, {self.y}"
