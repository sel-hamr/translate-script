import sys
from Translator import handle_translate
from utils import check_args, get_text_and_lang, handle_exit

def main():
    try:
        args = check_args()
        print(args)
        if args.get('text') is not None:
         handle_translate(args["text"], args["lang"])
        else:
            while True:
                text, lang = get_text_and_lang()
                handle_translate(text, lang)
                handle_exit()        
    except Exception as e:
        print(e)
        sys.exit(1)
        
if __name__ == "__main__":
    main()