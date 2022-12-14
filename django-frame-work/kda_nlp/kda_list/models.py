from django.db import models

class KdaList(models.Model):
    use_in_migration = True
    time = models.AutoField(primary_key=True)
    kda = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    aii_kill = models.IntegerField() # ally involved in killing 킬관여아군
    eii_kill = models.IntegerField() # enemy involved in killing 킬관여적군
    category = models.TextField()
    match_id = models.IntegerField()

    class Meta:
        db_table = "kda_list"

    def __str__(self):
        return f"{self.pk}, {self.time}, {self.kda}, {self.x}, {self.y}" \
               f"{self.aii_kill}, {self.eii_kill}, {self.category}, {self.match_id}"

