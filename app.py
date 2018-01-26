import csv
import random

def read_questions(num):
    question_id = []
    strand_dict = {}
    
    set_strand_val = 1
    
    with open('questions.csv', 'r') as questions_file:
        reader = csv.DictReader(questions_file)
        for row in reader:
            strand_dict['question ' + row['question_id']] = row['strand_id']
        print(strand_dict)
        
    for i in range(0,num):
        select_question = (random.sample(list(strand_dict),1))
        
        while strand_dict[select_question[0]] == set_strand_val:
            select_question = (random.sample(list(strand_dict),1))
        set_strand_val = strand_dict[select_question[0]]
        question_id.append(select_question)
        
    for q in question_id:
        print(q[0])
        

def take_user_input():
    print('Please enter number of questions for the quiz')
    num_ques = int(input())
    if num_ques <= 0:
        print('This input is invalid, please enter valid number of questions')
        take_user_input()
    else:
        print('Great work, here are the questions')
        
    return num_ques
    
inp = take_user_input()

read_questions(inp)