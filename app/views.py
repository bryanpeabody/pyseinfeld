from __future__ import print_function
from datetime import datetime
from flask import render_template, session, request, redirect
from random import randint
from app import app

import sys


# Globals
# This should be in a DB but since I'm just playing around, this will do for now.
questions = [  
        {             
			'id': 1,
			'question': 'What is the definition of Frolf?',
            'optionA': 'The term George uses to instead of vomit',
			'optionB': 'A combination of golf and fribee',
			'optionC': 'The name of Kramer''s goldfish', 
			'optionD': 'Elaine''s favorite brand of sponge', 
			'answer': 'B'
        },
		{             
			'id': 2,
			'question': 'What are the names of the ''Bizarro'' friends Elaine meets?',
            'optionA': 'Frank, Sid, and Micheal',
			'optionB': 'Kevin, Gene, and Feldman', 
			'optionC': 'Pete, Sid, and Nuncan', 
			'optionD': 'Herman, Greg, and Monty', 
			'answer': 'B'
        },
		{             
			'id': 3,
			'question': 'What are the names of the street tuffs that harass Kramer?',
            'optionA': 'Raul and Chicano', 
			'optionB': 'Martin and Jose', 
			'optionC': 'Cedric and Bob', 
			'optionD': 'Dylan and Paul', 
			'answer': 'C'
        },
		{             
			'id': 4,
			'question': 'What is the one sure-fire way to open Elaine''s vault?',
            'optionA': 'Blackmail', 
			'optionB': 'A "down payment"', 
			'optionC': 'Slipping her a roofie', 
			'optionD': 'With schnapps', 
			'answer': 'D'
        },
		{             
			'id': 5,
			'question': 'How long was Jerry''s "throw-up streak?"',
            'optionA': 'Since kindergarten', 
			'optionB': 'Thirty-six days', 
			'optionC': 'Fourteen years', 
			'optionD': 'Since his 21st birthday',
			'answer': 'C'
        },
        {
        	'id': 6,
			'question': 'In "The Mango", which market was Jerry banned from?',
            'optionA': 'John\'s Fruit Stand', 
			'optionB': 'Mike\'s Fruit Stand', 
			'optionC': 'Joe\'s Fruit Stand', 
			'optionD': 'Tim\'s Fruit Stand',
			'answer': 'C'
        },
        {
        	'id': 7,
			'question': 'In "The Glasses", it turns out what was kissing the girl George mistook for Jerry\'s girlfriend Amy ?',
            'optionA': 'A Horse', 
			'optionB': 'A Dog', 
			'optionC': 'A Hobo', 
			'optionD': 'A Pole',
			'answer': 'A'
        },
        {
        	'id': 8,
			'question': 'On which show does Jerry appear on in "The Puffy Shirt" ?',
            'optionA': 'The Early Show', 
			'optionB': 'The Today Show', 
			'optionC': 'The Morning Show', 
			'optionD': 'Good Morning America',
			'answer': 'B'
        },
        {
        	'id': 9,
			'question': 'In "The Sniffing Accountant", Elaine is annoyed when her boyfriend, Jake, forgets to put what on a note he left for her ?',
            'optionA': 'A Name', 
			'optionB': 'An Exclamation Point', 
			'optionC': 'The Date and Time', 
			'optionD': 'A Question Mark',
			'answer': 'B'
        },
        {
        	'id': 10,
			'question': 'In "The Lip Reader", which famous female tennis player is competing during Kramer\'s first time being a ball boy ?',
            'optionA': 'Steffi Graf', 
			'optionB': 'Mary Pierce', 
			'optionC': 'Monica Seles', 
			'optionD': 'Jennifer Capriati',
			'answer': 'C'
        },
        {
        	'id': 11,
			'question': 'In "The Non-Fat Yogurt", what did George say he banged his elbow on, to make it have the spasms ?',
            'optionA': 'A desk', 
			'optionB': 'A door', 
			'optionC': 'A table', 
			'optionD': 'A kitchen counter',
			'answer': 'A'
        },
        {
        	'id': 12,
			'question': 'In "The Barber", when Pensky asked why he took the smaller office, what was George\'s reason ?',
            'optionA': 'He didn\'t want to "Impose" on anyone', 
			'optionB': 'He was afraid of big spaces', 
			'optionC': 'He was afraid of people watching him through the windows', 
			'optionD': 'He could get more work done, less to distract him',
			'answer': 'D'
        },
        {
        	'id': 13,
			'question': 'In "The Masseuse", Elaine\'s boyfriend, Joel Rifkin, decides to change his name. What is NOT a name Elaine suggested to Joel ?',
            'optionA': 'Remy Rifkin', 
			'optionB': 'Alex Rifkin', 
			'optionC': 'Stewart Rifkin', 
			'optionD': 'Deon Rifkin',
			'answer': 'B'
        },
        {
        	'id': 14,
			'question': 'In "The Cigar Stor Indian", who is on the cover of the TV guide Elaine takes from Frank\'s house ?',
            'optionA': 'Kelsey Grammar', 
			'optionB': 'Martha Stewart', 
			'optionC': 'Tom Brokaw', 
			'optionD': 'Al Roker',
			'answer': 'D'
        },
        {
        	'id': 15,
			'question': 'In "The Conversion", which religion does George plan to convert to ?',
            'optionA': 'Moravarian Orthodox', 
			'optionB': 'Lusitanian Orthodox', 
			'optionC': 'Latvian Orthodox', 
			'optionD': 'Greek Orthodox',
			'answer': 'C'
        },
        {
        	'id': 16,
			'question': 'In "The Marine Biologist", Kramer shoots what type of golf ball into the whale ?',
            'optionA': 'A Slazenger', 
			'optionB': 'A Srixon', 
			'optionC': 'A Callaway', 
			'optionD': 'A Titleist',
			'answer': 'D'
        },
        {
        	'id': 17,
			'question': 'In "The Dinner Party", Jerry and Elaine have to settle for which desert to bring to the dinner party ?',
            'optionA': 'Cinnamon Bobka', 
			'optionB': 'Blackforest Cake', 
			'optionC': 'Chocolate Bobka', 
			'optionD': 'Carrot Cake',
			'answer': 'A'
        },
        {
        	'id': 18,
			'question': 'In "The Pie", Jerry obsesses over his girlfriend not eating what type of pie ?',
            'optionA': 'Blueberry Pie', 
			'optionB': 'Cherry Pie', 
			'optionC': 'Apple Pie', 
			'optionD': 'Pecan Pie',
			'answer': 'C'
        },
        {
        	'id': 19,
			'question': 'In “The Stand-In”, which soap opera was Kramer and Mickey doing stand ins for ?',
            'optionA': 'Days of Our Lives', 
			'optionB': 'All My Children', 
			'optionC': 'The Young and the Restless', 
			'optionD': 'Passions',
			'answer': 'B'
        },
        {
        	'id': 20,
			'question': 'In “The Wife”, Elaine’s health club boyfriend wants to turn George in because he broke what policy ?',
            'optionA': 'Stealing another person\'s glasses', 
			'optionB': 'Leaving sweat on the workout machine', 
			'optionC': 'Peeing in the shower', 
			'optionD': 'Leaving the treadmill on',
			'answer': 'C'
        },
        {
        	'id': 21,
			'question': 'In “The Fire”, Elaine’s annoying co-worker’s toe gets cut off. Which one gets cut off ?',
            'optionA': 'The Big Toe', 
			'optionB': 'The Middle Toe', 
			'optionC': 'The Ring Toe', 
			'optionD': 'The Pinky Toe',
			'answer': 'D'
        },
        {
        	'id': 22,
			'question': 'In “The Hamptons”, Elaine is perplexed when the doctor says the ugly baby is what ?',
            'optionA': 'Breathtaking', 
			'optionB': 'Gorgeous', 
			'optionC': 'Adorable', 
			'optionD': 'Stunning',
			'answer': 'A'
        },
        {
        	'id': 23,
			'question': 'In “The Opposite”, since George is doing everything opposite, he orders the opposite of food too. Instead of getting a tuna sandwich, what type of sandwich does he get ?',
            'optionA': 'Salmon Sandwich', 
			'optionB': 'Ham Sandwich', 
			'optionC': 'Chicken Salad Sanchwich', 
			'optionD': 'Turkey Sandwich',
			'answer': 'C'
        },
        {
        	'id': 24,
			'question': 'The "The Scoflaw", who is the white whale?',
            'optionA': 'Kramer', 
			'optionB': 'Uncle Leo', 
			'optionC': 'Jerry', 
			'optionD': 'Newman',
			'answer': 'D'
        },
        {
        	'id': 25,
			'question': 'In "The Little Jerry", what was little Jerry?',
            'optionA': 'Kramer\'s pet rooster', 
			'optionB': 'Kramer\'s pet chicken', 
			'optionC': 'A picture of Jerry as a little kid', 
			'optionD': 'A Macoroni statue of Jerry',
			'answer': 'A'
        },
        {
        	'id': 26,
			'question': 'What kind of pasta does Kramer make a Jerry figurine from ?',
            'optionA': 'Penne', 
			'optionB': 'Fusilli', 
			'optionC': 'Tortellini', 
			'optionD': 'Angel Hair',
			'answer': 'B'
        }
    ]
    
total_questions = len(questions)      

@app.route('/')
def index():	
	print(total_questions)
	# Setup/reset data that will be in the session
	shown_questions = []	
	total_correct = 0
	
	session["shown_questions"] = shown_questions	
	session["total_correct"] = total_correct
	
	return render_template('index.html')

@app.route("/getCorrectAnswer", methods=['POST'])
def getCorrectAnswer():
	# Get the quesiton id from the post
	question_id = int(request.form['question_id'])
	
	# Fine the question id and return the correct answer
	return questions[question_id-1]['answer']

@app.route("/save", methods=['POST'])
def save():
	# Get the POST parameters
	question_id = int(request.form['question_id'])
	isCorrect = int(request.form['isCorrect'])	
		
	# if the user got it correct, incrememnt the count
	if isCorrect == 1:
		total_correct = session["total_correct"]
		total_correct = total_correct + 1			
		session["total_correct"] = total_correct
	
	# Go to the next question
	return "OK"
	
@app.route("/play")						
def play():
	# Pull the total correct and shown questions from the session
	shown_questions	= session["shown_questions"]
	total_correct = session["total_correct"]
	
	# Are we finished?
	if (len(shown_questions) == total_questions):
		return redirect("/finish")
	
	# Get the next random question
	question_id = randint(0,total_questions-1)
	
	# Have we shown this question? If so, find another one
	while question_id in shown_questions:
		question_id = randint(0,len(questions)-1)
	
	# Set the question we will pass to the view
	question = questions[question_id]
	shown_questions.append(question_id)
	session["shown_questions"] = shown_questions	
	
	# Get the current question count for the view
	question_number = len(shown_questions)
	
	return render_template('play.html',
							question=question,
							question_number=question_number,
							total_questions=total_questions)


@app.route("/finish")
def finish():	
	# Get the total correct answers from session
	total_correct = session["total_correct"]
	
	# View data
	percent = 0
	imageToShow = "bad.png"
	
	# Figure out the percentage and which image class to show
	if total_correct != 0:
		percent = (total_correct / total_questions) * 100
		
		if percent == 100:
			imageToShow = "perfect.png"
		elif percent >= 70:
			imageToShow = "so-so.png"
		
	return render_template('finish.html',
							percent=percent,
							imageToShow=imageToShow)
		
# Secret key for session	
app.secret_key = 'CosmoKramer'