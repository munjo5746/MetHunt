from django.db import models

# Create your models here.
class Hunt(models.Model):
    """
    This is the Hunt model. A Hunt has many items that is related to the
    specific hunt.
    """

    # django automatilcally add id as primary key.. Use this to get each Hunt.
    Title = models.CharField(max_length = 100)
    # This Questions will be string that is formatted in json.
    # The json data will be list of Question id from start to the end.
    Items = models.CharField(max_length = 100)


    def __str__(self):
        return self.Title


class Item(models.Model):
    """
    Question is belong to one of the Hunt. One Hunt should have multiple
    questions, and each question can belong to multiple hunts. In each Hunt,
    we need to keep the order of questions from start to the end. One easy way
    to do is make a list attribute in Hunt.
    """
    # define custome primary with the met's id.
    QuestionId = models.CharField(primary_key = True, unique = True, max_length = 50)
    Category = models.CharField(max_length = 50)
    BelongTo = models.ManyToManyField(Hunt)
    Clue = models.CharField(max_length = 100)
    # this represent the locatio of the art in the muserum
    Location = models.CharField(max_length = 300)
