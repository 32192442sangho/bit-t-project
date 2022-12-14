from django.db import models

from kda_nlp.kda_list.models import KdaList
from kill_analysis.ashoutput.models import AshOutput
from main.users.models import Users
from ward_places.min_output.models import MinOutput


# Create your models here.



class GameList(models.Model):
    use_in_migrations = True
    match_id = models.CharField(max_length=20, primary_key=True, unique=True)
    champion = models.IntegerField(max_length=10)
    kda = models.CharField(max_length=10)
    game_result = models.IntegerField(max_length=10)
    x_coordinate = models.IntegerField(max_length=10)
    y_coordinate = models.IntegerField(max_length=10)
    nlp_qs = models.TextField()
    nlp_ans = models.TextField()
    nlp_ans_type = models.IntegerField(max_length=30)
    k_d_a = models.IntegerField(max_length=10)
    kda_type = models.IntegerField(max_length=10)
    user_id = models.CharField(max_length=20)

    nickname = models.ForeignKey(Users, on_delete=models.CASCADE)
    time = models.ForeignKey(KdaList, on_delete=models.CASCADE)
    user_death_id = models.ForeignKey(AshOutput, on_delete=models.CASCADE)
    ward_coordinate_id = models.ForeignKey(MinOutput, on_delete=models.CASCADE)

    class Meta:
        db_table = "gamelists"

    def __str__(self):
        return f"{self.pk} {self.match_id} {self.champion} {self.kda} {self.game_result} " \
               f"{self.x_coordinate} {self.y_coordinate} {self.nlp_qs} {self.nlp_ans}" \
               f"{self.nlp_ans_type} {self.k_d_a} {self.kda_type} {self.user_id} {self.nickname}" \
               f"{self.time} {self.user_death_id} {self.ward_coordinate_id}  "