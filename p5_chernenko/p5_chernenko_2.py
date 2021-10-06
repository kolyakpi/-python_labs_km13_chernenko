input_str = input("Input a sequence of words: ")

words = []
word = ""
print(type(input_str))
for i in range(len(input_str)):
    if input_str[i] != " ":
        word += input_str[i]
    else:
        words.append(word)
        word = ""
words.append(word)

sentence = ""
for i in range(len(words)):
    if words[i] == "and":
        sentence += " and "
    else:
        sentence += words[i]
    if words[i] != "and":
        if i != len(words) - 1:
            if words[i+1] != 'and':
                sentence += ", "

print(sentence)
