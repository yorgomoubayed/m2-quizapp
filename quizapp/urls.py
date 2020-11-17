from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('login/', views.loginpage, name='quiz-login'),
    path('logout/', views.logoutuser, name='quiz-logout'),
    path('register/', views.registerpage, name='quiz-register'),

    path('exploresem/', views.exploresem, name='quiz-exploresem'),
    path('exploretem/', views.exploretem, name='quiz-exploretem'),
    path('explorephase/', views.explorephase, name='quiz-explorephase'),
    path('exploreillumination/', views.exploreillumination, name='quiz-exploreillumination'),
    path('exploredetection/', views.exploredetection, name='quiz-exploredetection'),
    path('explorefluorescence/', views.explorefluorescence, name='quiz-explorefluorescence'),

    path('quizlab/', views.quizlab, name='quiz-quizlab'),
    path('microscopyquiz/', views.microscopyquiz, name='quiz-microscopyquiz'),
    path('microscopyquiz/microscopyquizend/', views.microscopyquizend, name='quiz-microscopyquizend'),
    path('featuresquiz/', views.featuresquiz, name='quiz-featuresquiz'),
    path('featuresquiz/featuresquizend/', views.featuresquizend, name='quiz-featuresquizend'),
]