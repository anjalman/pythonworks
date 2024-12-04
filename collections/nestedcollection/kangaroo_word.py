
source_word = "CHICKEN"
target_word = "HEN"

# step1 find source_word character count

# create a empty dicto

# character_count={}

# for ch in source_word:

#     if ch in character_count:

#         character_count[ch]+=1

#     else:

#         character_count[ch]=1

# print(character_count)

character_count={ch:source_word.count(ch) for ch in source_word}

# print(character_count)
is_kangaroo_word=True

for ch in target_word:
    
    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1

    else:
        is_kangaroo_word=False

        break

print(is_kangaroo_word)
