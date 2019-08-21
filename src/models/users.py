from django.db import models

class Asset(models.Model):
   id        = models.AutoField(primary_key=True)
   name      = models.CharField(max_length=50, default="N/A")
   email_id  = models.CharField(max_length=50,default="N/A")
   age       = models.IntegerField(default=18)
   gender    = models.CharField(max_length=6, default="Common")
   password  = models.CharField(max_length=30, default="")
   salt      = models.CharField(max_length=20, default="")

   def save(self, *args, **kwargs):
       return super(Asset, self).save(*args, **kwargs)

   def __unicode__(self):
       return str(self.id)

   class Meta:
       db_table = 'users'
       app_label = 'src'