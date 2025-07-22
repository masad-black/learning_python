from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

"""
curd operations
    (create): there are different ways to create a model object
    1: model_name.objects.create(field1=value1, field2=value2, ...), not need to call save()

    2: my_obj = model_name(field1=value1, field2=value2, ...)
       my_obj.save()

    3: my_dict = {"field1": value1, "field2": value2, ...} 
         model_name.objects.create(**my_dict)
    
    (read): there are different ways to read a object from the database
    1: model_name.objects.all() # get all objects
    2: model_name.objects.filter(field1=value1) # get all objects that match the filter
    3: model_name.objects.get(field1=value1) # get a single object that matches the filter
       # if no object found, it will raise DoesNotExist exception
    4: model_name.objects.first() # get the first object
    5: model_name.objects.last() # get the last object

    (update):
    1: my doing it manually
    my_obj = model_name.objects.get(field1=value1)
       my_obj.field2 = new_value
       my_obj.save()
    2: using the update fn
    model_name.objects.filter(field1=value1).update(field2=new_value)

    (delete):
    1: my_obj = model_name.objects.get(field1=value1)
       my_obj.delete()
    2: model_name.objects.filter(field1=value1).delete() # delete all objects
    3: model_name.objects.all().delete() # delete all objects
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # this fn help for making the model_name.objects.get() method more readable
    # this is called by
    def __str__(self):
        return "{} published on {}".format(
            self.question_text, self.pub_date.strftime("%Y-%m-%d %H:%M:%S")
        )

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
