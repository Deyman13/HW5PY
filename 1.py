# 1 способ
string = input().split(" ")
for word in string:
    if "абв".lower() in word.lower():
        string.remove(word)
print(" ".join(string))

# 2 способ
string = input().split(" ")
string = list(filter(lambda x: "абв" not in x.lower(), string))
print(" ".join(string))

# 3 способ
print(" ".join(list(filter(lambda x: "абв" not in x.casefold(), input().split(" ")))))

