from django.db import models

class KdaList(models.Model):
    use_in_migration = True
    time = models.AutoField(primary_key=True, max_length=30)
    kda = models.IntegerField(max_length=10)
    x = models.IntegerField(max_length=10)
    y = models.IntegerField(max_length=10)
    aii_kill = models.IntegerField(max_length=10) # ally involved in killing 킬관여아군
    eii_kill = models.IntegerField(max_length=10) # enemy involved in killing 킬관여적군
    category = models.TextField()
    match_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "kda_list"

    def __str__(self):
        return f"{self.pk}, {self.time}, {self.kda}, {self.x}, {self.y}" \
               f"{self.aii_kill}, {self.eii_kill}, {self.category}, {self.match_id}"

