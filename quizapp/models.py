from django.db import models

class questions(models.Model):
    question_id = models.IntegerField(blank=True)
    question = models.CharField(blank=True, max_length=600)
    category = models.CharField(blank=True, max_length=600)
    image_no = models.IntegerField(blank=True)
    answers_no = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)
    image = models.CharField(blank=True, max_length=600)

class answers(models.Model):
    question_no = models.IntegerField(blank=True)
    #=question_id = models.ForeignKey(questions, on_delete=models.CASCADE)
    question_id = models.IntegerField(blank=True)
    answer = models.CharField(blank=True, max_length=600)
    definition = models.TextField(blank=True, max_length=800)

class images(models.Model):
    image_id = models.IntegerField()
    image_name = models.IntegerField()
    image_description = models.TextField(blank=True, max_length=1000)
    image_mode = models.CharField(max_length=600)
    cell_type = models.CharField(max_length=600)
    component = models.CharField(max_length=600)
    organism = models.CharField(max_length=600)
    doi = models.CharField(max_length=600)

    class Meta:
        db_table = 'quizapp_images'

