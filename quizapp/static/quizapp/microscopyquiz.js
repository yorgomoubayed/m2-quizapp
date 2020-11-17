const question = document.querySelector('#question');
const choices = Array.from(document.querySelectorAll('.choice-text'));
const progressText = document.querySelector('#progressText');
const scoreText = document.querySelector('#score');
const progressBarFull = document.querySelector('#progressBarFull');
const image = document.createElement('#img')

let currentQuestion = {}
let acceptingAnswers = true
let score = 0
let questionCounter = 0
let availableQuestions = []

let questions = [
    {
        question: 'Which type of microscopy was used to take these images?',
        choice1: 'Fluorescence microscopy',
        choice2: 'Scanning electron microscopy',
        choice3: 'Transmission electron microscopy',
        choice4: 'Phase contrast microscopy',
        answer: 2,
    },
    {
        question: 'Which type of microscopy was used to take these images?',
        choice1: 'Fluorescence microscopy',
        choice2: 'Scanning electron microscopy',
        choice3: 'Transmission electron microscopy',
        choice4: 'Phase contrast microscopy',
        answer: 1,
    },
    {
        question: 'Which type of microscopy was used to take these images?',
        choice1: 'Fluorescence microscopy',
        choice2: 'Scanning electron microscopy',
        choice3: 'Transmission electron microscopy',
        choice4: 'Phase contrast microscopy',
        answer: 3,
    },
    {
        question: 'Which type of microscopy was used to take these images?',
        choice1: 'Fluorescence microscopy',
        choice2: 'Scanning electron microscopy',
        choice3: 'Transmission electron microscopy',
        choice4: 'Phase contrast microscopy',
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

        return window.location.assign("microscopyquizend/")
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