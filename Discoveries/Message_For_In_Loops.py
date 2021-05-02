Thought = input('How do i look like? ')

Mean  = [ 'ugly', 'hideous', 'nerd', 'moron', 'stupid' ]
for i in Mean:
    if f"{i}" in Thought.lower():
        print ("You look like one too")
        break
    if f"{i}" not in Thought.lower():
        print ("Well thanks.")
        break

# Learned: For In Loop Breaks