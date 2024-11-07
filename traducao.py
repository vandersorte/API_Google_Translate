from deep_translator import GoogleTranslator

text_en = 'Starting a company is like throwing yourself off the cliff and assembling an airplane on the way down.'

def traduzir(text):
  tradutor = GoogleTranslator(source='en', target='pt')
  traducao = tradutor.translate(text)
  return traducao

print(traduzir(text_en))

