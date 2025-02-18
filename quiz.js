// Quiz Questions (You can easily add more)
const questions = [
    {
        question: "What is 2 + 2?",
        options: ["3", "4", "5", "6"],
        answer: "4"
    },
    {
        question: "What is the capital of France?",
        options: ["Berlin", "Madrid", "Paris", "Rome"],
        answer: "Paris"
    },
    {
        question: "Which planet is known as the Red Planet?",
        options: ["Earth", "Mars", "Jupiter", "Venus"],
        answer: "Mars"
    }
];

// Load questions into the page
function loadQuestions() {
    const quizContent = document.getElementById('quiz-content');
    questions.forEach((question, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.classList.add('question');
        
        const questionText = document.createElement('p');
        questionText.innerText = question.question;
        questionDiv.appendChild(questionText);

        const optionsList = document.createElement('ul');
        optionsList.classList.add('options');

        question.options.forEach(option => {
            const optionLi = document.createElement('li');
            const radioInput = document.createElement('input');
            radioInput.type = 'radio';
            radioInput.name = `question-${index}`;
            radioInput.value = option;
            const label = document.createElement('label');
            label.innerText = option;
            optionLi.appendChild(radioInput);
            optionLi.appendChild(label);
            optionsList.appendChild(optionLi);
        });

        questionDiv.appendChild(optionsList);
        quizContent.appendChild(questionDiv);
    });
}

// Submit quiz and calculate score
function submitQuiz() {
    let score = 0;
    const results = [];

    // Loop through each question and check answers
    questions.forEach((question, index) => {
        const selectedOption = document.querySelector(`input[name="question-${index}"]:checked`);
        if (selectedOption) {
            if (selectedOption.value === question.answer) {
                score++;
            }
        }
    });

    // Display results
    const resultDiv = document.getElementById('result');
    resultDiv.innerText = `You scored ${score} out of ${questions.length}!`;

    // Optional: Apply a cool transition for results
    resultDiv.style.transition = "opacity 0.5s ease-in-out";
    resultDiv.style.opacity = "1";
}

// Initialize quiz
window.onload = loadQuestions;
