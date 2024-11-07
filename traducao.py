from deep_translator import GoogleTranslator

text_in_English = 'Starting a company is like throwing yourself off the cliff and assembling an airplane on the way down.'

def translate_function(text):
  translator = GoogleTranslator(source='en', target='pt')
  translated_text = translator.translate(text)
  return translated_text

print(translate_function(text_in_English))

