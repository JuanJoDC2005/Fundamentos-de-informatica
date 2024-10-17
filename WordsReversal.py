
input_sentence = input("Please enter a sentence: ")

words = input_sentence.split()

reversed_words = words[::-1]

reversed_sentence = ' '.join(reversed_words)

print("Reversed sentence:", reversed_sentence)
