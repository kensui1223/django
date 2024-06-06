from django.db import models
class Gakuseikanri(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    enumber = models.CharField(max_length=15)
    eemail = models.EmailField()

    def __str__(self):
        return "%s " %(self.ename)
    class Meta:
        db_table = "gakuseikanri"