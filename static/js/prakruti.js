const questions = [
    {
        'id': 'kapha_question1',
        'question': 'Whether your skin remains oily throughout the year in comparison to others?',
        'attribute': 'kapha',
        'yes_points': 120,
        'no_points': 0,

    },
    {
        'id': 'kapha_question2',
        'question': 'Are your body-hairs & skin shiny, even no oil or moisturizer is used?',
        'attribute': 'kapha',
        'yes_points': 120,
        'no_points': 0,

    },
    {
        'id': 'kapha_question3',
        'question': 'Are you considered attractive among your friends?',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question4',
        'question': 'Do even mild or trivial injuries on your body make you upset?',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question5',
        'question': 'Among your family members, Is your complexion considered fairer?',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question6',
        'question': 'Do you think you have intense sexual desire ?',
        'attribute': 'kapha',
        'yes_points': 120,
        'no_points': 0,

    },

    {
        'id': 'kapha_question7',
        'question': 'Have got well built muscles?',
        'attribute': 'kapha',
        'yes_points': 60,
        'no_points': 0,

    },
    {
        'id': 'kapha_question8',
        'question': 'Do you change your body posture frequently? (You cannot manage yourself in a single posture for longer duration) ?',
        'attribute': 'kapha',
        'yes_points': 0,
        'no_points': 60,

    },
    {
        'id': 'kapha_question9',
        'question': 'Do you have well-nourished normally developed body? (You are neither malnourished nor obese)',
        'attribute': 'kapha',
        'yes_points': 120,
        'no_points': 0,

    },
    {
        'id': 'kapha_question10',
        'question': 'Are you lazy and disinterested in activities like morning walk/jogging , swimming or any type of outdoor games ?',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question11',
        'question': 'Are you slow in consuming food?(Even all have left the dining hall, you are still consuming the same amount of food.',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question12',
        'question': 'When you to morning walk or college or office, do walk slowly in comparison to others?',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question13',
        'question': 'If you are assigned any work, do you take some estra time to start it?',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question14',
        'question': "Do you get imitated easily? (For example, when you don't get breaktast on time in your hostel or when the power goes off while watching a cricket match or your favorite movie on television)",
        'attribute': 'kapha',
        'yes_points': 0,
        'no_points': 40,

    },
    {
        'id': 'kapha_question15',
        'question': 'Are you late to develop suffer from symptoms after exposure to common causative factors? (For example, during seasonal changes, when your friends are easily caught up with flu etc., you are still healthy among them)',
        'attribute': 'kapha',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'kapha_question16',
        'question': 'Does your gait (style of walking) change with respect to speed or manner frequently?',
        'attribute': 'kapha',
        'yes_points': 0,
        'no_points': 120,

    },
    {
        'id': 'kapha_question17',
        'question': 'Do you feel hungry more frequently and do you? consume more food in comparison to others?',
        'attribute': 'kapha',
        'yes_points': 0,
        'no_points': 30,

    },
    {
        'id': 'kapha_question18',
        'question': 'Do you tolerate heat easily?',
        'attribute': 'kapha',
        'yes_points': 30,
        'no_points': 0,

    },
    {
        'id': 'kapha_question19',
        'question': 'Do you consume liquids in more quantity and frequency in comparison to others? ',
        'attribute': 'kapha',
        'yes_points': 0,
        'no_points': 30,

    },
    {
        'id': 'kapha_question20',
        'question': 'Do you perspire less in comparison to others?',
        'attribute': 'kapha',
        'yes_points': 30,
        'no_points': 0,

    },
    {
        'id': 'kapha_question21',
        'question': 'Are sounds produced frequently in your joints on movements?',
        'attribute': 'kapha',
        'yes_points': 0,
        'no_points': 120,

    },
    {
        'id': 'kapha_question22',
        'question': 'Have you got a good/attractive complexion?',
        'attribute': 'kapha',
        'yes_points': 60,
        'no_points': 0,

    },
    {
        'id': 'kapha_question23',
        'question': 'Have you got sweet & pleasant voice?',
        'attribute': 'kapha',
        'yes_points': 60,
        'no_points': 0,

    },
    {
        'id': 'pitta_question1',
        'question': 'Are you more comfortable in winter than summers?',
        'attribute': 'pitta',
        'yes_points': 17,
        'no_points': 0,

    },
    {
        'id': 'pitta_question2',
        'question': 'Among your family members, is your complexion considered fairer? ',
        'attribute': 'pitta',
        'yes_points': 17,
        'no_points': 0,

    },
    {
        'id': 'pitta_question3',
        'question': 'Does your temperature of oral cavity remain towards upper limit of normal range?',
        'attribute': 'pitta',
        'yes_points': 17,
        'no_points': 0,

    },
    {
        'id': 'pitta_question4',
        'question': 'Do you have excessive black moles. Freckles etc ou your skin? Or Have you noticed new appearance of black moles often on your skin?',
        'attribute': 'pitta',
        'yes_points': 17,
        'no_points': 0,

    },
    {
        'id': 'pitta_question5',
        'question': 'Do you feel excessive hunger & thirst in comparison to others?',
        'attribute': 'pitta',
        'yes_points': 17,
        'no_points': 0,

    },
    {
        'id': 'pitta_question6',
        'question': 'Have you experienced premature graying, wrinkling of skin & early baldness?',
        'attribute': 'kapha',
        'yes_points': 17,
        'no_points': 0,

    },
    {
        'id': 'kapha_question7',
        'question': 'Do you have soft, scanty, brown hair on your face. body & head?',
        'attribute': 'kapha',
        'yes_points': 17,
        'no_points': 0,

    },
    {
        'id': 'kapha_question8',
        'question': 'Do you involve yourself in risky & heroic activities requiring physical strength often?',
        'attribute': 'kapha',
        'yes_points': 24,
        'no_points': 0,

    },
    {
        'id': 'kapha_question9',
        'question': 'Do you have ability to digest lage quantities of food easily?',
        'attribute': 'kapha',
        'yes_points': 24,
        'no_points': 0,

    },
    {
        'id': 'kapha_question10',
        'question': 'Do you take large quantities of food & drink in comparison to others?',
        'attribute': 'kapha',
        'yes_points': 24,
        'no_points': 0,

    },
    {
        'id': 'kapha_question11',
        'question': 'Do you have soft, scanty, brown hair on your face. body & head?',
        'attribute': 'kapha',
        'yes_points': 24,
        'no_points': 0,

    },
    {
        'id': 'kapha_question12',
        'question': 'Do you get easily irritated for small/negligible problem in day-to-day life?',
        'attribute': 'kapha',
        'yes_points': 24,
        'no_points': 0,

    },
    {
        'id': 'kapha_question13',
        'question': 'Do you consume food more frequently than others? (5-6 times/day)',
        'attribute': 'kapha',
        'yes_points': 24,
        'no_points': 0,

    },
    {
        'id': 'kapha_question14',
        'question': ' Do you have soft & loose muscle bulk especially around the joints?',
        'attribute': 'kapha',
        'yes_points': 60,
        'no_points': 0,

    },
    {
        'id': 'kapha_question15',
        'question': 'In comparison to others do you pass urine & stool in large quantities and do you perspire more? ',
        'attribute': 'kapha',
        'yes_points': 60,
        'no_points': 0,

    },
    {
        'id': 'kapha_question16',
        'question': 'Do your friends complain about bad smell being emitted from mouth or body?',
        'attribute': 'kapha',
        'yes_points': 120,
        'no_points': 0,

    },
    {
        'id': 'kapha_question17',
        'question': 'Do you think you have intense sexual desire? ',
        'attribute': 'kapha',
        'yes_points': 0,
        'no_points': 120,

    },
    {
        'id': 'vata_question1',
        'question': 'Whether your skin remains dry throughout the year in comparison to others?',
        'attribute': 'vata',
        'yes_points': 30,
        'no_points': 0,

    },
    {
        'id': 'vata_question2',
        'question': 'Is your body undernourished/emaciated ?',
        'attribute': 'vata',
        'yes_points': 30,
        'no_points': 0,

    },
    {
        'id': 'vata_question3',
        'question': 'Have you got rough, low, broken or obstructed voice Does Your sleep last less than 6 hours per day Or you sleep can be disturbed easily?',
        'attribute': 'vata',
        'yes_points': 30,
        'no_points': 0,

    },
    {
        'id': 'vata_question4',
        'question': 'Do you change walking speed & style from time to time?',
        'attribute': 'vata',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'vata_question5',
        'question': 'Do you keep changing your food habits from time to time? ',
        'attribute': 'vata',
        'yes_points': 40,
        'no_points': 0,

    },
    {
        'id': 'vata_question6',
        'question': 'Do you keep changingyour walking / jogging habit from time to time?',
        'attribute': 'vata',
        'yes_points': 40,
        'no_points': 0,

    },

    {
        'id': 'vata_question7',
        'question': 'Do you keep your joints, eyes, eyebrows, jaw, lips. tongue, head, Shoulder, hands & feet frequently moving?',
        'attribute': 'vata',
        'yes_points': 120,
        'no_points': 0,

    },
    {
        'id': 'vata_question8',
        'question': 'Are you considered a talkative among your friends?',
        'attribute': 'vata',
        'yes_points': 60,
        'no_points': 0,

    },
    {
        'id': 'vata_question9',
        'question': 'Do you have prominent veins & tendons all over the body?',
        'attribute': 'vata',
        'yes_points': 60,
        'no_points': 0,

    },
    {
        'id': 'vata_question10',
        'question': 'Do you generally start the work assigned to you immediately?',
        'attribute': 'vata',
        'yes_points': 15,
        'no_points': 0,

    },
    {
        'id': 'vata_question11',
        'question': 'Do you get irritated easily? (E.g., when you do not get breakfast on time in your hostel or when the power goes off while watching a cricket match on your TV ?',
        'attribute': 'vata',
        'yes_points': 15,
        'no_points': 0,

    },



]

let crossBtn = document.getElementById("cross-btn");
let errorMsgElem = document.getElementById("error-message");

let msgContent = document.getElementById("mess-content");
let iVal = 0;
let arrLength = questions.length;
let messBtn = document.getElementById("mess-btn");

function displayQuestion(index) {
    msgContent.innerHTML = `
        <p>${questions[index].question}</p>
    `;
}

displayQuestion(iVal);

messBtn.addEventListener("click", function () {
    iVal++;
    if (iVal < arrLength) {
        displayQuestion(iVal);
    } else {
        // All questions have been asked! 
    }
});

// Simulate user responses as an object (you can replace this with actual user input)
const userResponses = {
  kapha_question1: 1, // User's response for the first question
  // Add responses for other questions
};

// Initialize scores
let vata_score = 0;
let pitta_score = 0;
let kapha_score = 0;

// Calculate scores based on user responses
questions.forEach((question) => {
  const response = userResponses[question.id];

  if (response !== undefined) {
    if (question.attribute === 'vata') {
      vata_score += response * question.yes_points;
    } else if (question.attribute === 'pitta') {
      pitta_score += response * question.yes_points;
    } else if (question.attribute === 'kapha') {
      kapha_score += response * question.yes_points;
    }
  } else {
    vata_score += 0;
    pitta_score += 0;
    kapha_score += 0;
  }
});

// Determine Prakruti type
let prakruti_type = '';
if (vata_score > pitta_score && vata_score > kapha_score) {
  prakruti_type = 'Vata Prakruti';
} else if (pitta_score > vata_score && pitta_score > kapha_score) {
  prakruti_type = 'Pitta Prakruti';
} else {
  prakruti_type = 'Kapha Prakruti';
}

// The variable 'prakruti_type' now contains the determined Prakruti type
console.log('Prakruti Type: ' + prakruti_type);


crossBtn.addEventListener("click", function () {
    errorMsgElem.style.display = "none";

})

document.addEventListener("DOMContentLoaded", function () {

    // Setting timeout for n Seconds
    setTimeout(() => {
        if (errorMsgElem) {
            errorMsgElem.style.display = "none";
        }
    }, 5000);


})



const messagesList = document.querySelector('.messages-list');
const messageForm = document.querySelector('.message-form');
const messageInput = document.querySelector('.message-input');

messageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    if (message.length === 0) {
        return;
    }

    const messageItem = document.createElement('li');
    messageItem.classList.add('message', 'sent');
    messageItem.innerHTML = `
      <div class="message-text">
          <div class="message-sender">
              <b>You</b>
          </div>
          <div class="message-content">
              ${message}
          </div>
      </div>`;
    messagesList.appendChild(messageItem);

    messageInput.value = '';

});


