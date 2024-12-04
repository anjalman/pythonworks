

text="Hello world Hello everyone.Welcome to the world."

word=text.split()

word_frequancy={w:word.count(w)for w in word}

print(max(word_frequancy))


