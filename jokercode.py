import pyjokes
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='tr')

original_joke = pyjokes.get_joke()

translated_joke = translator.translate(original_joke)

print("Original Joke:")
print(original_joke)
print("\nTranslated Joke:")
print(translated_joke)



