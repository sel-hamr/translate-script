from translate import Translator

def translate_text(text,lang = "es"):
    try:
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return e
    
def check_lang(lang):
    supported_lang = ["es","fr","de","it","pt","nl","pl","ru","ja","zh-CN","ko","tr","ar"]
    if lang in supported_lang:
        return True
    else:
        return False

def handle_translate(text, lang):
    try:
        if check_lang(lang):
            translation = translate_text(text, lang)
            print(translation)
        else :
            raise Exception('Language not supported. Supported languages are: es, fr, de, it, pt, nl, pl, ru, ja, zh-CN, ko, tr, ar') 
    except Exception as e:
        print(e)