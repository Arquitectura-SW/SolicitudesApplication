from django.db import models 

class Solicitud(models.Model):
    user = models.IntegerField(default = None, null=False)
    creationDate = models.DateTimeField(auto_now_add = True)
    closeDate = models.DateField(null = True, blank= True, default = None)
    status = models.CharField(max_length = 50)

    def __str__(self):
        return '%s %s %s %s' % (str(self.user), self.creationDate, self.status, self.closeDate)
