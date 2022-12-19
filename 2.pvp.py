from random import randint as r


def takecandy(name):
    taken_candy = int(
        input(f"{name} сколько конфет хочешь забрать от 1 до 28? "))
    while taken_candy < 1 or taken_candy > 28:
        taken_candy = int(input(f"{name} попробуй еще раз. От 1 до 28! "))
    return taken_candy


player1 = input("Первый игрок: ")
player2 = input("Второй игрок: ")
candy = int(input("Сколько конфет на столе? "))
step = r(0, 2)
print(f"{player1 if step == 1 else player2} Ходит первым!")

while candy > 28:
    taken = takecandy(player1) if step == 1 else takecandy(player2)
    candy -= taken
    step += 1 if step < 1 else -1
    print(f"{player2 if step == 1 else player1} взял {taken} конфет. Осталось {candy}.")
print(f'Победил: {player1 if step == 1 else player2}, забрав последние {candy} конфет и тем самым все остальные! Поздравляем!!!')
