Thought = input('How do i look like? ')

Compliment = [ 'good', 'handsome', 'alluring', 'attractive' ]
for i in Compliment:
    if Thought.lower() == f"{i}":
        print ('Woah thank you.')
        break
    if Thought.lower() != f"{i}":
        print ('Ok.')
        break