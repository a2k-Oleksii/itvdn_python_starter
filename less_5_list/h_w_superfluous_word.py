a = ['red', 'yellow', 'blue', 'bread']
superfluous_word = []
colors = ['red', 'yellow', 'blue', 'black', 'orange', 'purple']

for element in a:
    for colors_element in colors:
        if element == colors_element:
            break
        else:
            superfluous_word.append(element)

print(superfluous_word)
