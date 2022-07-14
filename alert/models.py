from django.contrib.auth.models import User
from django.db import models

StatusChioce=(
("created", "created"),
("deleted", "deleted"),
("triggered", "triggered"),
)

# Create your models here.



class Base(models.Model):
  """
  _summary_
  Base model Includes the timeframes and models Inheritance

  """
  created_at= models.DateTimeField(auto_now_add=True)
  modified_at= models.DateTimeField(auto_now=True)
  deleted_at= models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Alert(Base):
  price = models.DecimalField(max_digits=19, decimal_places=2)
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="alerts")
  status = models.CharField(choices=StatusChioce,max_length=20,default="created")    

  def __str__(self):
    return self.user.username