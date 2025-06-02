from django.db import models

# Create your models here.
class hesabketab (models.Model):
    HESABKETAB_TYPE=(
        ('income','omad'),
        ('expense','raft'),
    )
    txtTitle = models.CharField(max_length=255)
    amount=models.BigIntegerField()
    hesabketab_type=models.CharField(max_length=255,choices=HESABKETAB_TYPE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.txtTitle} - {self.hesabketab_type} - {self.amount}"




