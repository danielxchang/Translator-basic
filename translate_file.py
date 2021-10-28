from translate import Translator


language = "fr"
translator = Translator(to_lang = language)

try:
    with open("./test.txt", mode="r") as my_file:
        text = my_file.read()
    translation = translator.translate(text)
    print(translation)
    with open(f"./test-{language}.txt", mode="w") as my_file2:
        my_file2.write(translation)
except FileNotFoundError as err:
    print("File does not exist")
    raise err
except IOError as err:
    print("IO Error")
    raise err
