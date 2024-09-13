import sys

def check_args():
    if len(sys.argv) == 4:
        print("error: should not have more than 2 argument")
        sys.exit(1)
    elif len(sys.argv) == 2:
        return {
            "text": sys.argv[1],
            "lang": "es"
        }
    elif len(sys.argv) == 3:
        return {
            "text": sys.argv[1],
            "lang": sys.argv[2]
        }
    else: 
        return {
            "text": None,
            "lang": None
        }
      
def get_text_and_lang():
    text = input("Enter text to translate: ")
    lang = input("Enter language to translate to: ")
    return text, lang

def handle_exit():
    action = input("Press Enter to continue or type 'exit' to quit: ")
    if action == "exit":
        sys.exit(0)