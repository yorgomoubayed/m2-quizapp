from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import answers, questions, images

def home(request):
    return render(request, 'quizapp/home.html')

def quizlab(request):

    first_answers_obj = answers.objects.filter(question_id=1)
    second_answers_obj = answers.objects.filter(question_id=2)
    first_questions_obj = questions.objects.filter(question_id=1)
    second_questions_obj = questions.objects.filter(question_id=2)

    quizlab_context = {
        'first_answers_items': first_answers_obj,
        'second_answers_items': second_answers_obj,
        'first_questions_items': first_questions_obj,
        'second_questions_items': second_questions_obj,
    }

    return render(request, 'quizapp/quizlab.html', quizlab_context)

def registerpage(request):
#    if request.user.is_authenticated:
#        return redirect('quiz-home')
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('quiz-login')

        register_context = {'form': form}
        return render(request, 'quizapp/register.html', register_context)

def loginpage(request):
#    if request.user.is_authenticated:
 #       return redirect('quiz-home')
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('quiz-home')

            else:
                messages.info(request, 'username or password is incorrect')

        login_context = {}
        return render(request, 'quizapp/login.html', login_context)

def logoutuser(request):
    logout(request)
    return redirect('quiz-login')

def exploresem(request):
    sem_obj = images.objects.filter(image_mode='scanning electron microscopy (SEM)')
    sem_context = {
        'sem_items': sem_obj
    }
    return render(request, 'quizapp/exploresem.html', sem_context)

def exploretem(request):
    tem_obj = images.objects.filter(image_mode='transmission electron microscopy (TEM)')
    tem_context = {
        'tem_items': tem_obj
    }
    return render(request, 'quizapp/exploretem.html', tem_context)

def explorefluorescence(request):
    fluorescence_obj = images.objects.filter(image_mode='fluorescence microscopy')
    fluorescence_context = {
        'fluorescence_items': fluorescence_obj
    }
    return render(request, 'quizapp/explorefluorescence.html', fluorescence_context)

def explorephase(request):
    phase_obj = images.objects.filter(image_mode='phase contrast microscopy')
    phase_context = {
        'phase_items': phase_obj
    }
    return render(request, 'quizapp/explorephase.html', phase_context)

def exploreillumination(request):
    illumination_obj = images.objects.filter(image_mode='illumination by electrons')
    illumination_context = {
       'illumination_items': illumination_obj
    }
    return render(request, 'quizapp/exploreillumination.html', illumination_context)

def exploredetection(request):
    detection_obj = images.objects.filter(image_mode='detection of electrons')
    detection_context = {
       'detection_items': detection_obj
    }
    return render(request, 'quizapp/exploredetection.html', detection_context)

def quiz(request):
    return render(request, 'quizapp/game.html')

def microscopyquiz(request):
    return render(request, 'quizapp/microscopyquiz.html')

def microscopyquizend(request):
    return render(request, 'quizapp/microscopyquizend.html')

def featuresquiz(request):
    return render(request, 'quizapp/featuresquiz.html')

def featuresquizend(request):
    return render(request, 'quizapp/featuresquizend.html')

#supplement
    # q1 = questions.objects.filter(question_id=1)
    # q2 = questions.objects.filter(question_id=2)
    #
    # index_context = {
    # 'q1': q1,
    # 'q2': q2,
    # }

    # q1 = questions.objects.filter(question_id=1)
    # q2 = questions.objects.filter(question_id=2)
    #
    # index_context = {
    # 'q1': q1,
    # 'q2': q2,
    # }