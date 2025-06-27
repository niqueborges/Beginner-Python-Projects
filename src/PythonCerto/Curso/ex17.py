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

# primeiro crie um arquivo de exmplo
#echo "This is a test file." > test.txt
# então dê uma olhada nele
# cat test.txt
# agora execute seu script nele