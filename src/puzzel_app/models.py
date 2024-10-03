from django.db import models

class PageVisit(models.Model):
    #db  -> table(rows and columns)
    #id -> hidden -> primary key -> autofield -> 1, 2, 3, 4, 5 till infinite
    
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
