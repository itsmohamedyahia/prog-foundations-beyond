first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize'
first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()
print(first_name_cap + " " + last_name_cap)
# prints first occurence of location of first character that is a part of that string
# rfind prints last occurence
award_location = note.find('award: ')
# if output is -1, that means find didnt find this string
print(award_location)
award_name = note[7:]  # from character nom 7 to end of the string
print(award_name)
