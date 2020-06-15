from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    local = models.CharField(max_length=50, default='Centro')
    image = models.ImageField(upload_to='images/services')
    services_done = models .IntegerField (default=1)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')