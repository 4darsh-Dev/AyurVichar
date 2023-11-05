from django.shortcuts import render, redirect

# added by adarsh

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# from django.http import HttpResponse

from .models import PrakrutiResult

from .forms import PrakrutiForm

# Create your views here.

def index(request):
    return render(request, "index.html") 

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html" )

def contact(request):
    return render(request, "contact.html")

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Matching user credentials
        user = authenticate(username = username, password = password)

        if user is not None:
            # dj authenticating id and pass
            login(request, user)
     
            return redirect('/prakruti') 

        else:
            # No backend authenticated the credentials
            error_message = "Invalid username or password! Please try again."
            messages.error(request, error_message)
            
            # return render(request, 'login.html')
            return render(request, "login.html", {"error_message" : error_message} )
        
    return render(request, "login.html")


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("cnf-password")

        # Check for username 
        if len(username) >10:
            error_msg1 = "Username must not be more than 10 characters"
            messages.error(request, error_msg1)

            return render(request, "signup.html", {"error_message" : error_msg1})
        
        # check for alphanumeric 
        if (not username.isalnum()):
            error_msg2 = "Username must be alpha-numeric"
            messages.error(request, error_msg2)

            return render(request, "register.html", {"error_message": error_msg2})
        
        # Checking for passwords match
        if pass1 != pass2:
            error_msg3 = "Passwords don't match!"
            messages.error(request, error_msg3)

            return render(request, "register.html", {"error_message" : error_msg3})
        
        # Checking for already existing users
        if (User.objects.filter(username=username).exists()):
            error_msg4 = "Username already taken! Please choose different one."
            messages.error(request, error_msg4)
            return render(request, "register.html", {"error_message": error_msg4})
        
        # Check for duplicated email 
        if (User.objects.filter(email=email).exists()):
            error_msg5 = "Email already taken! Please choose different one."
            messages.error(request, error_msg5)
            return render(request, "register.html", {"error_message ": error_msg5})
        
        # Creating user
        myUser = User.objects.create_user(username, email, pass2)
        myUser.save()
        success_msg = "Your a/c has been created successfully! "
        messages.success(request, success_msg)

        return redirect('/prakruti')
    
    return render(request, "register.html")

def logoutUser(request):
    auth.logout(request)
    return redirect("home")


def profile(request):

    return render(request, "profile.html" )



# def prakruti(request):
#     return render(request, "prakruti.html")


def prakriti_request(request):
    
    questions = [
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
    
    if request.method == 'POST':
        form = PrakrutiForm(request.POST)
        if form.is_valid():
            prakruti_result = form.save(commit=False)
            vata_score = 0
            pitta_score = 0
            kapha_score = 0

            for question in questions:
                response = request.POST.get(question['id'])
                if response == 'yes':
                    if question['attribute'] == 'vata':
                        vata_score += question['yes_points']
                    elif question['attribute'] == 'pitta':
                        pitta_score += question['yes_points']
                    elif question['attribute'] == 'kapha':
                        kapha_score += question['yes_points']

            # Determine Prakruti type
            if vata_score > pitta_score and vata_score > kapha_score:
                prakruti_result.prakruti_type = "Vata Prakruti"
            elif pitta_score > vata_score and pitta_score > kapha_score:
                prakruti_result.prakruti_type = "Pitta Prakruti"
            else:
                prakruti_result.prakruti_type = "Kapha Prakruti"

            prakruti_result.user = request.user  # Assuming you have user authentication
            prakruti_result.vata_score = vata_score
            prakruti_result.pitta_score = pitta_score
            prakruti_result.kapha_score = kapha_score
            prakruti_result.save()

            return redirect('profile')  # Redirect to a success page or profile page

    else:
        form = PrakrutiForm()

    return render(request, 'prakruti-chatbot.html', {'questions': questions, 'form': form})









