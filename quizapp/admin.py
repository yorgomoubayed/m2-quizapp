from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from quizapp.models import images, answers, questions

@admin.register(images)
@admin.register(questions)
@admin.register(answers)

class imagesadmin(ImportExportModelAdmin):
    list_display_1 = ("image_id",
                    "image_name",
                    "image_description",
                    "image_mode",
                    "cell_type",
                    "component",
                    "organism",
                    "doi")
    pass

class answersadmin(ImportExportModelAdmin):
    list_display_2 = ("question_no",
                      "question_id",
                      "answer",
                      "definition")
    pass

class questionsadmin(ImportExportModelAdmin):
    list_display_3 = ("question_id",
                      "question",
                      "category",
                      "image_no",
                      "answers_no",
                      "points",
                      "image")
    pass