import random
responses = ['Seems so','Never','Untrue','Always no matter what','You decide your fate','Not sure','Yep','Nope','Maybe','Nein','Qui','Ask the person next to you','That question is not for me']

def answer():
    question = input('Ask me anything: ')
    print(random.choice(responses))
answer()

secondQuestion = (input('Another question? Yes/No: '))
while secondQuestion == str('Yes'):
    answer()
    secondQuestion = (input('Another question? Yes/No: '))
                     
else:                                               
    print('Thank you for asking the wise magic 8 ball')
