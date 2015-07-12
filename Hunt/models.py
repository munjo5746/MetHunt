from django.db import models

# Create your models here.
class Hunt(models.Model):
    """
    This is the Hunt model. A Hunt has many items that is related to the
    specific hunt.
    """

    title = models.CharField(max_length = 50)
    
