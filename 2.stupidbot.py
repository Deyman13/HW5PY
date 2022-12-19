from random import randint as r


def takecandy(name):
    taken_candy = int(
        input(f"{name} сколько конфет хочешь забрать от 1 до 28? "))
    while taken_candy < 1 or taken_candy > 28:
        taken_candy = int(input(f"{name} попробуй еще раз. От 1 до 28! "))
    return taken_candy


name = input("Как тебя зовут? ")
bot = "Тупоголовый"
candy = int(input("Количество конфет на столе: "))
step = r(0, 2)
print(f"{name if step == 1 else bot} Ходит первым!")
while candy > 28:
    taken = takecandy(name) if step == 1 else r(1, 29)
    candy -= taken
    step += 1 if step < 1 else -1
    print(f"{bot if step == 1 else name} взял {taken} конфет. Осталось {candy}.")
print(f'Победил: {name if step == 1 else bot}, забрав последние {candy} конфет и тем самым все остальные! Поздравляем!!!')
