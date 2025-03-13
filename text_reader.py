# read in text file
# I downloaded a .txt file of filler text from https://sample-files.com/documents/txt/
# and saved it into the pands-weekly-tasks folder as long_doc.txt

# according to W3 schools documentation, r for read and t for text are default value so I'm not specifiying
with open(r"C:\Users\fmtie\Desktop\pands-weekly-tasks\long_doc.txt") as file:
    content = file.read()

character = 'e'

num_e = content.count(character)

print(f"The character {character} occurs {num_e} times in the text file.")



