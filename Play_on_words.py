import random

my_file = (open('C:/Users/User/Desktop/слова.txt'))
text = my_file.read()
my_file.close()
words = []
available_words = list(words)
for word in text.split():
    words.append(word)
    available_words = list(words)
    random.shuffle(available_words)
    anyword = available_words.pop()
print("Рандомное слово " + anyword)


def playing(anyword):
    game_is_over = False
    while not game_is_over:
        mess = input()
        if mess:
            if anyword[-1] in ["ъ", "ь", "ы"]:
                if anyword[-2] == mess.lower()[0]:
                    print(anyword)
                    for candidant in available_words:
                        if candidant.lower()[0] == mess.lower()[-1]:
                            anyword = candidant
                            print(anyword)
                            available_words.remove(candidant)
                            break
                else:
                    print(
                        "Неверно, слово должно начинаться с буквы " + anyword[-2])
            elif mess.lower()[0] != anyword.lower()[-1]:
                print(
                    "Неверно, слово должно начинаться с буквы " + anyword[-1])
            else:
                for candidant in available_words:
                    if candidant.lower()[0] == mess.lower()[-1]:
                        anyword = candidant
                        print(anyword)
                        available_words.remove(candidant)
                        break
                    elif mess.lower()[-1] in ["ъ", "ь", "ы"]:
                        if candidant[0].lower() == mess[-2].lower():
                            anyword = candidant
                            print(anyword)
                            available_words.remove(candidant)
                            break
                else:
                    print("Словарный запас был исчерпан, схожу за новой порцией.")
                    game_is_over = True
        else:
            print("Введите слово")


playing(anyword)
