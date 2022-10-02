from googletrans import Translator as google_translator
from translate import Translator as offline_translator

# With google translator
g_translator = google_translator()
try:
    with open('text_en.txt', 'r', encoding="utf-8") as file_en:
        text_en = file_en.read()
        text_ja = g_translator.translate(text_en, src='en', dest='ja').text
        with open('text_ja_g.txt', 'w', encoding="utf-8") as file_ja:
            file_ja.write(text_ja)
except FileNotFoundError as err:
    print(err)


# With offline translator
o_translator = offline_translator(to_lang='ja')
try:
    with open('text_en.txt', 'r', encoding="utf-8") as file_en:
        text_en = file_en.read()
        text_ja = o_translator.translate(text_en)
        with open('text_ja_o.txt', 'w', encoding="utf-8") as file_ja:
            file_ja.write(text_ja)
except FileNotFoundError as err:
    print(err)
