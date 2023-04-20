#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = []

if spam == [] :
    print('This is an empty list.')
elif len(spam) == 1 :
    print(spam[0])
else :
    item = 0
    while item < len(spam) :
        if item == 0 :
            print(spam[item], end = '')
        elif item == len(spam) - 1 :
            print(' and ' + spam[item])
        else :
            print(', ' + spam[item], end='')
        item += 1
