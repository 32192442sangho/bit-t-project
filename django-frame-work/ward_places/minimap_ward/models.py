from django.db import models


class MinimapWard(models.Model):
    use_in_migration = True

    time = models.AutoField(primary_key=True)
    team = models.IntegerField()
    ward_place = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    champion_count = models.IntegerField()
    ward_type = models.IntegerField()
    control_count = models.IntegerField()
    ward_duration = models.IntegerField() # 와드 지속 시간

    class Meta:
        db_table = "minimap_ward"

    def __str__(self):
        return f"{self.pk}, {self.team}, {self.ward_place}, {self.x}, {self.y}" \
               f"{self.champion_count}, {self.ward_type}, {self.control_count}, {self.ward_duration}"
