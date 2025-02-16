from textblob import TextBlob

def correct_grammar(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

text = input('enter your sentence: ')
corrected_text = correct_grammar(text)
print(f'corrected: {corrected_text}')