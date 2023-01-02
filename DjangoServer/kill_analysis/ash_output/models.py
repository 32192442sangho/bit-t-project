from django.db import models




# Create your models here.
class AshOutput(models.Model):
    use_in_migrations = True
    user_death_id = models.IntegerField(max_length=10, primary_key=True)
    death_reason = models.TextField()

    class Meta:
        db_table = "AshOutputs"

    def __str__(self):
        return f"{self.pk} {self.death_reason}"