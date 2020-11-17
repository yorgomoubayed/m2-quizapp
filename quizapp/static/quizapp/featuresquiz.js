const question = document.querySelector('#question');
const choices = Array.from(document.querySelectorAll('.choice-text'));
const progressText = document.querySelector('#progressText');
const scoreText = document.querySelector('#score');
const progressBarFull = document.querySelector('#progressBarFull');
/*const image1 = document.createElement('#image1')
const image2 = document.createElement('#image2')*/


let currentQuestion = {}
let acceptingAnswers = true
let score = 0
let questionCounter = 0
let availableQuestions = []

let questions = [
    {
        question: 'Which feature is common between the images?',
/*        image1 : "{% static 'quizapp/images/214.jpg' %}",
        image2 : "static/quizapp/images/187.jpg",*/
        choice1: 'Axoneme',
        choice2: 'Synaptic vesile',
        choice3: 'Pollen wall',
        choice4: 'Desmosome',
        answer: 2,
    },
    {
        question: "Which feature is common between the images?",
        choice1: 'Axoneme',
        choice2: 'Synaptic vesile',
        choice3: 'Pollen wall',
        choice4: 'Desmosome',
        answer: 1,
    },
    {
        question: "Which feature is common between the images?",
        choice1: 'Axoneme',
        choice2: 'Synaptic vesile',
        choice3: 'Pollen wall',
        choice4: 'Desmosome',
        answer: 3,
    },
    {
        question: "Which feature is common between the images?",
        choice1: 'Axoneme',
        choice2: 'Synaptic vesile',
        choice3: 'Pollen wall',
        choice4: 'Desmosome',
        answer: 1,
    }
]

const SCORE_POINTS = 3
const MAX_QUESTIONS = 4

startGame = () => {
    questionCounter = 0
    score = 0
    availableQuestions = [...questions]
    getNewQuestion()
}

getNewQuestion = () => {
    if(availableQuestions.length === 0 || questionCounter > MAX_QUESTIONS) {
        localStorage.setItem('mostRecentScore', score)

        return window.location.assign("featuresquizend/")
    }

    questionCounter++
    progressText.innerText = `Question ${questionCounter} of ${MAX_QUESTIONS}`
    progressBarFull.style.width = `${(questionCounter/MAX_QUESTIONS) * 100}%`

    const questionsIndex = Math.floor(Math.random() * availableQuestions.length)
    currentQuestion = availableQuestions[questionsIndex]
    question.innerText = currentQuestion.question

    choices.forEach(choice => {
        const number = choice.dataset['number']
        choice.innerText = currentQuestion['choice' + number]
    })

    availableQuestions.splice(questionsIndex, 1)

    acceptingAnswers = true
}

choices.forEach(choice => {
    choice.addEventListener('click', e => {
        if(!acceptingAnswers) return

        acceptingAnswers = false
        const selectedChoice = e.target
        const selectedAnswer = selectedChoice.dataset['number']

        let classToApply = selectedAnswer == currentQuestion.answer ? 'correct' : 'incorrect'

        if(classToApply === 'correct') {
            incrementScore(SCORE_POINTS)
        }

        selectedChoice.parentElement.classList.add(classToApply)

        setTimeout(() => {
            selectedChoice.parentElement.classList.remove(classToApply)
            getNewQuestion()

        }, 1000)
    })
})

incrementScore = num => {
    score +=num
    scoreText.innerText = score
}

startGame()