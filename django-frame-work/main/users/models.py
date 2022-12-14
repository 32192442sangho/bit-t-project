from django.db import models

class Users(models.Model):
    use_in_migration = True
    nickname = models.AutoField(primary_key=True)
    puuid = models.UUIDField()

    class Meta:
        db_table = "play_users"

    def __str__(self):
        return f"{self.pk}, {self.puuid}"