from django.db import models


class MinimapWard(models.Model):
    use_in_migration = True

    time = models.AutoField(primary_key=True)
    team = models.IntegerField(max_length=10)
    ward_place = models.IntegerField(max_length=10)
    x = models.IntegerField(max_length=10)
    y = models.IntegerField(max_length=10)
    champion_count = models.IntegerField(max_length=10)
    ward_type = models.IntegerField(max_length=10)
    control_count = models.IntegerField(max_length=10)
    ward_duration = models.IntegerField(max_length=10) # 와드 지속 시간

    class Meta:
        db_table = "minimap_ward"

    def __str__(self):
        return f"{self.pk}, {self.team}, {self.ward_place}, {self.x}, {self.y}" \
               f"{self.champion_count}, {self.ward_type}, {self.control_count}, {self.ward_duration}"
