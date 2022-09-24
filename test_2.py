#some_text = "asdefgdfsgdfvdffdf"
#print(len(some_text))
#first_index = 0
#last_index = (len(some_text) - 1)
#print(some_text[first_index])
##print(some_text[last_index])

#word = input()
#go = len(word)
#print(go)

#name = "Petyr Ivanov"
#name_without_whitespaces = ""
#for character in name:
    #print(character)

name = 'Petyr Ivanov'
name_without_whitespaces = ""
for character in name:
    if character != ' ':
        name_without_whitespaces += character
print(name_without_whitespaces)
# ime bez interval
name = "petar ivanov"
name = name.replace(' ', "")
print(name)
# ime bez interval