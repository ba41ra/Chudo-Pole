secret_word = input("Введите слово для игры:")
print("\033[2J")
win = False
true_letters = []
all_letters = []
points = [0, 0, 0]
counter = 0
while win == False:
    letter = input(f"\nИгрок номер {counter + 1} ваша буква...?")
    if letter in all_letters:
        print("Эта буква уже была использована. Увы...")
    elif letter in secret_word:
        print(f"Вы отгадали букву {letter}, откройте нам её:")
        points[counter] +=1
        true_letters.append(letter)
        all_letters.append(letter)
    else:
        print("Такой буквы в этом слове нет...")
        all_letters.append(letter)
    win = True       
    for current_letter in secret_word:
        if current_letter in true_letters:
            print(current_letter, end="")
        else:
            print("*", end="")  
            win = False 
    counter += 1 
    if counter == 3:
        counter = 0
for index in range(3):
    print(f"\nИгрок №{index + 1} ваши очки:{points[index]}")  
