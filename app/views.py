from __future__ import print_function
from datetime import datetime
from flask import render_template, session, request, redirect
from random import randint
from app import app

import sys
import math

# Globals
# This should be in a DB but since I'm just playing around, this will do for now.
questions = [  
        {             
			'id': 1,
			'question': 'What is the definition of Frolf?',
            'optionA': 'A) The term George uses to instead of vomit',
			'optionB': 'B) A combination of golf and fribee',
			'optionC': 'C) The name of Kramer''s goldfish', 
			'optionD': 'D) Elaine''s favorite brand of sponge', 
			'answer': 'B'
        },
		{             
			'id': 2,
			'question': 'What are the names of the ''Bizarro'' friends Elaine meets?',
            'optionA': 'A) Frank, Sid, and Micheal',
			'optionB': 'B) Kevin, Gene, and Feldman', 
			'optionC': 'C) Pete, Sid, and Nuncan', 
			'optionD': 'D) Herman, Greg, and Monty', 
			'answer': 'B'
        },
		{             
			'id': 3,
			'question': 'What are the names of the street tuffs that harass Kramer?',
            'optionA': 'A) Raul and Chicano', 
			'optionB': 'B) Martin and Jose', 
			'optionC': 'C) Cedric and Bob', 
			'optionD': 'D) Dylan and Paul', 
			'answer': 'C'
        },
		{             
			'id': 4,
			'question': 'What is the one sure-fire way to open Elaine''s vault?',
            'optionA': 'A) Blackmail', 
			'optionB': 'B) A "down payment"', 
			'optionC': 'C) Slipping her a roofie', 
			'optionD': 'D) With schnapps', 
			'answer': 'D'
        },
		{             
			'id': 5,
			'question': 'How long was Jerry''s "throw-up streak?"',
            'optionA': 'A) Since kindergarten', 
			'optionB': 'B) Thirty-six days', 
			'optionC': 'C) Fourteen years', 
			'optionD': 'D) Since his 21st birthday',
			'answer': 'C'
        },
        {
        	'id': 6,
			'question': 'In "The Mango", which market was Jerry banned from?',
            'optionA': 'A) John\'s Fruit Stand', 
			'optionB': 'B) Mike\'s Fruit Stand', 
			'optionC': 'C) Joe\'s Fruit Stand', 
			'optionD': 'D) Tim\'s Fruit Stand',
			'answer': 'C'
        },
        {
        	'id': 7,
			'question': 'In "The Glasses", it turns out what was kissing the girl George mistook for Jerry\'s girlfriend Amy ?',
            'optionA': 'A) A Horse', 
			'optionB': 'B) A Dog', 
			'optionC': 'C) A Hobo', 
			'optionD': 'D) A Pole',
			'answer': 'A'
        },
        {
        	'id': 8,
			'question': 'On which show does Jerry appear on in "The Puffy Shirt" ?',
            'optionA': 'A) The Early Show', 
			'optionB': 'B) The Today Show', 
			'optionC': 'C) The Morning Show', 
			'optionD': 'D) Good Morning America',
			'answer': 'B'
        },
        {
        	'id': 9,
			'question': 'In "The Sniffing Accountant", Elaine is annoyed when her boyfriend, Jake, forgets to put what on a note he left for her ?',
            'optionA': 'A) A Name', 
			'optionB': 'B) An Exclamation Point', 
			'optionC': 'C) The Date and Time', 
			'optionD': 'D) A Question Mark',
			'answer': 'B'
        },
        {
        	'id': 10,
			'question': 'In "The Lip Reader", which famous female tennis player is competing during Kramer\'s first time being a ball boy ?',
            'optionA': 'A) Steffi Graf', 
			'optionB': 'B) Mary Pierce', 
			'optionC': 'C) Monica Seles', 
			'optionD': 'D) Jennifer Capriati',
			'answer': 'C'
        },
        {
        	'id': 11,
			'question': 'In "The Non-Fat Yogurt", what did George say he banged his elbow on, to make it have the spasms ?',
            'optionA': 'A) A desk', 
			'optionB': 'B) A door', 
			'optionC': 'C) A table', 
			'optionD': 'D) A kitchen counter',
			'answer': 'A'
        },
        {
        	'id': 12,
			'question': 'In "The Barber", when Pensky asked why he took the smaller office, what was George\'s reason ?',
            'optionA': 'A) He didn\'t want to "Impose" on anyone', 
			'optionB': 'B) He was afraid of big spaces', 
			'optionC': 'C) He was afraid of people watching him through the windows', 
			'optionD': 'D) He could get more work done, less to distract him',
			'answer': 'D'
        },
        {
        	'id': 13,
			'question': 'In "The Masseuse", Elaine\'s boyfriend, Joel Rifkin, decides to change his name. What is NOT a name Elaine suggested to Joel ?',
            'optionA': 'A) Remy Rifkin', 
			'optionB': 'B) Alex Rifkin', 
			'optionC': 'C) Stewart Rifkin', 
			'optionD': 'D) Deon Rifkin',
			'answer': 'B'
        },
        {
        	'id': 14,
			'question': 'In "The Cigar Stor Indian", who is on the cover of the TV guide Elaine takes from Frank\'s house ?',
            'optionA': 'A) Kelsey Grammar', 
			'optionB': 'B) Martha Stewart', 
			'optionC': 'C) Tom Brokaw', 
			'optionD': 'D) Al Roker',
			'answer': 'D'
        },
        {
        	'id': 15,
			'question': 'In "The Conversion", which religion does George plan to convert to ?',
            'optionA': 'A) Moravarian Orthodox', 
			'optionB': 'B) Lusitanian Orthodox', 
			'optionC': 'C) Latvian Orthodox', 
			'optionD': 'D) Greek Orthodox',
			'answer': 'C'
        },
        {
        	'id': 16,
			'question': 'In "The Marine Biologist", Kramer shoots what type of golf ball into the whale ?',
            'optionA': 'A) A Slazenger', 
			'optionB': 'B) A Srixon', 
			'optionC': 'C) A Callaway', 
			'optionD': 'D) A Titleist',
			'answer': 'D'
        },
        {
        	'id': 17,
			'question': 'In "The Dinner Party", Jerry and Elaine have to settle for which desert to bring to the dinner party ?',
            'optionA': 'A) Cinnamon Bobka', 
			'optionB': 'B) Blackforest Cake', 
			'optionC': 'C) Chocolate Bobka', 
			'optionD': 'D) Carrot Cake',
			'answer': 'A'
        },
        {
        	'id': 18,
			'question': 'In "The Pie", Jerry obsesses over his girlfriend not eating what type of pie ?',
            'optionA': 'A) Blueberry Pie', 
			'optionB': 'B) Cherry Pie', 
			'optionC': 'C) Apple Pie', 
			'optionD': 'D) Pecan Pie',
			'answer': 'C'
        },
        {
        	'id': 19,
			'question': 'In “The Stand-In”, which soap opera was Kramer and Mickey doing stand ins for ?',
            'optionA': 'A) Days of Our Lives', 
			'optionB': 'B) All My Children', 
			'optionC': 'C) The Young and the Restless', 
			'optionD': 'D) Passions',
			'answer': 'B'
        },
        {
        	'id': 20,
			'question': 'In “The Wife”, Elaine’s health club boyfriend wants to turn George in because he broke what policy ?',
            'optionA': 'A) Stealing another person\'s glasses', 
			'optionB': 'B) Leaving sweat on the workout machine', 
			'optionC': 'C) Peeing in the shower', 
			'optionD': 'D) Leaving the treadmill on',
			'answer': 'C'
        },
        {
        	'id': 21,
			'question': 'In “The Fire”, Elaine’s annoying co-worker’s toe gets cut off. Which one gets cut off ?',
            'optionA': 'A) The Big Toe', 
			'optionB': 'B) The Middle Toe', 
			'optionC': 'C) The Ring Toe', 
			'optionD': 'D) The Pinky Toe',
			'answer': 'D'
        },
        {
        	'id': 22,
			'question': 'In “The Hamptons”, Elaine is perplexed when the doctor says the ugly baby is what ?',
            'optionA': 'A) Breathtaking', 
			'optionB': 'B) Gorgeous', 
			'optionC': 'C) Adorable', 
			'optionD': 'D) Stunning',
			'answer': 'A'
        },
        {
        	'id': 23,
			'question': 'In “The Opposite”, since George is doing everything opposite, he orders the opposite of food too. Instead of getting a tuna sandwich, what type of sandwich does he get ?',
            'optionA': 'A) Salmon Sandwich', 
			'optionB': 'B) Ham Sandwich', 
			'optionC': 'C) Chicken Salad Sanchwich', 
			'optionD': 'D) Turkey Sandwich',
			'answer': 'C'
        },
        {
        	'id': 24,
			'question': 'In "The Scofflaw", who is the white whale?',
            'optionA': 'A) Kramer', 
			'optionB': 'B) Uncle Leo', 
			'optionC': 'C) Jerry', 
			'optionD': 'D) Newman',
			'answer': 'D'
        },
        {
        	'id': 25,
			'question': 'In "The Little Jerry", what was little Jerry?',
            'optionA': 'A) Kramer\'s pet rooster', 
			'optionB': 'B) Kramer\'s pet chicken', 
			'optionC': 'C) A picture of Jerry as a little kid', 
			'optionD': 'D) A Macoroni statue of Jerry',
			'answer': 'A'
        },
        {
        	'id': 26,
			'question': 'What kind of pasta does Kramer make a Jerry figurine from ?',
            'optionA': 'A) Penne', 
			'optionB': 'B) Fusilli', 
			'optionC': 'C) Tortellini', 
			'optionD': 'D) Angel Hair',
			'answer': 'B'
        }
    ]
    
total_questions = len(questions)      

# Setup routes
@app.route('/')
def index():	
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
							percent=math.floor(percent),
							imageToShow=imageToShow)
		
# Secret key for session	
app.secret_key = 'CosmoKramer'