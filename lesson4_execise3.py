def sign(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0

#ーー動作確認ーー

print(sign(-134))
print(sign(0))
print(sign(3))
