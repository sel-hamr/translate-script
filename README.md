# Translate Script

**Translate Script** is a command-line tool written in Python that allows users to translate text into multiple languages. The script accepts text either through command-line arguments or interactive user input and translates it using the `translate` library.

## Features

- Command-line text translation.
- Interactive mode for continuous translations.
- Supports multiple languages: Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Dutch (nl), Polish (pl), Russian (ru), Japanese (ja), Chinese (zh-CN), Korean (ko), Turkish (tr), and Arabic (ar).
- Graceful handling of unsupported languages.

## Prerequisites

Make sure you have Python installed:

- Python 3.x
- Install the `translate` library:
  ```bash
  pip install translate
  ```

## INSTALLATION

1. Clone the repository:

   ```bash
   git clone https://github.com/sel-hamr/translate-script.git
   cd translate-script

   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-line Arguments

To translate text using command-line arguments, run the script with the following syntax:

```bash
python translate.py --text "Hello, world!" --to es
```

Replace the `--text` argument with the text you want to translate and the `--to` argument with the language code you want to translate to.

This command will translate "Hello, world!" into Spanish(`es`).

### Interactive Mode

If no arguments are provided, the script will enter an interactive mode, where you can input text and select a language for translation:

```bash
python main.py
```

The script will prompt you to enter the text and the target language interactively.

## Example

```bash
$ python main.py
Enter text to translate: Hello, how are you?
Enter language to translate to: fr
Translation: Bonjour, comment ça va?
Press Enter to continue or type 'exit' to quit: exit
```

## Error Handling

1. If the `translate` library does not support the target language, the script will display an error message and exit gracefully.

2. If the user enters an invalid language code, the script will display an error message and prompt the user to enter a valid language code.

3. If too many arguments are provided, the script will display an error message and exit.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
