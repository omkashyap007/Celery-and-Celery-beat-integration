from django.db import models


class News(models.Model):
    source_id                           = models.CharField(max_length = 50 , blank = True , null = True)
    source_name                         = models.CharField(max_length = 50 , blank = True , null = True)
    author                              = models.CharField(max_length = 100 ,  blank = False , null = False)
    title                               = models.CharField(max_length = 200 , blank = False , null = False)
    description                         = models.CharField(max_length = 200, blank = False, null = False)
    url                                 = models.URLField(blank = True , null = True)
    published_at                        = models.DateTimeField(blank = False , null = False)
    content                             = models.TextField(max_length = 1000 , blank = False , null = False)
    
    def __str__(self):
        return f"{self.title[:20]} : {self.author[:20]}"