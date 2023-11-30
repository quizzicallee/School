print('type the first word that comes to mind for each of the following prompts.')

#Assigned inputs

adjective = input('Adjective: ')
animal = input('Animal: ')
verb_1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb_2 = input('Verb: ')
verb_3 = input('Verb: ')

#Extra Inputs
adjective_2 = input('Adjective: ')
noun = input('Family Memeber:')
body_part = input('Body Part: ')
name = input('Name: ')
verb_4 = input('Verb: ')

#Story
print('Your story is: ')

mad_lib = f'''
The other day, I was really in trouble. It all started when I saw a very
{adjective.lower()} {animal.lower()} {verb_1.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb_2.lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb_3.lower()}
right in front of my family. I was {adjective_2.lower()} I couldnt look my 
{noun.capitalize()} in the {body_part.lower()}.
If only I had remembered {name.capitalize()} can {verb_4.lower()}. '''

print(f'{mad_lib}')