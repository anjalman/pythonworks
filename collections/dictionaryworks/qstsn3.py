
text="ABABBCCDDEH"

character_frequancy={ch:text.count(ch) for ch in text}

print(character_frequancy)

# for k,v in character_frequancy.items():

#     if v==1:

#         print(k)

non_recursive_character=[k for k,v in character_frequancy.items() if v==1]

print(non_recursive_character)
