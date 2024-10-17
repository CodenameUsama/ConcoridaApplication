# Note that you can analyse a text that's inputed by the user OR a pre-written text by unhashing line number 7 and hashing line number 6 


# # write file
input_file = open('input.txt', 'w')
input_file.write(input('\nPlease write a text to be analysed :\n'))
# input_file.write('''This is the input file''')
print('----------------------------')


# read input file
try:
    input_file = open('input.txt', 'r')
    print('File contains the next text:\n','"',input_file.read(),'"','\n----------------------------')
# error handling
except FileNotFoundError:
    print('''Cannot find 'input.txt'!''')
except OSError:
    print('Could not open/read file!')


# close input file
input_file.close()

# character(s) counter
with open("input.txt","r") as file:
    text = file.read()
    print('Number of character(s) in the file:\n',len(text),'character(s)','\n----------------------------')

#character(s) analyse:
    character_list = sorted(list(text.upper()))
    character_dict = {}
    for c in character_list:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    print('Character(s) analyse:')
    for k, v in character_dict.items():
        print(k, ':', v)

# close file
file.close()

# writing output file
output_file = open('output.txt', 'w')
string_dict = (str(character_dict))
split_dict = string_dict.replace(',', '\n')
output_file.write(split_dict.strip('{}'))