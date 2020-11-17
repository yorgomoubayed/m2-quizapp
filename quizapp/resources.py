from import_export import resources
from quizapp.models import images, answers, questions

class imagesresrouces(resources.ModelResource):
    class Meta:
        model1 = images

class questionsresrouces(resources.ModelResource):
        model2 = questions

class answersresrouces(resources.ModelResource):
        model3 = answers
