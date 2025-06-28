from sys import argv
# leia a seção O que Você Deve Ver para saber como executar isso
script, stuff, things, that = argv

print("The script is called:", script)
print("your first variable is:", stuff)
print("your second variable is:", things)
print("your third variable is:", that)

print('---')

from sys import argv
# leia a seção O que Você Deve Ver para saber como executar isso
script, apple, orange, grapefruit = argv

print("The script is called:", script)
print("your first variable is:", apple)
print("your second variable is:", orange)
print("your third variable is:", grapefruit)

print('---')

from sys import argv
# leia a seção O que Você Deve Ver para saber como executar isso
script, first, second, third = argv

print("The script is called:", script)
print("your first variable is:", first)
print("your second variable is:", second)
print("your third variable is:", third)

print('---')

from sys import argv

script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer Nice.
""")

print('---')

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

print('---')

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

print('---')

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# poderíamos fazer esses dois com uma linha, como?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Read, hit Return to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# primeiro crie um arquivo de exemplo
# echo "This is a test file." > test.txt
# então dê uma olhada nele
# cat test.txt
# agora execute seu script nele

print('---')



