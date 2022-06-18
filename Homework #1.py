from pprint import pprint

ST_TITLE = 1
ST_COUNT = 2
ST_INGREDIENTS = 3

cook_book = {}
state = ST_TITLE
with open('My_Files\list of ingridients.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        if state == ST_TITLE:
            title = line
            cook_book[title] = []
            state = ST_COUNT
        elif state == ST_COUNT:
            count = int(line)
            state = ST_INGREDIENTS
        else: # if state == ST_INGREDIENTS:
            data = [x.strip() for x in line.split('|')]
            data[1] = int(data[1])
            cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
            count -= 1
            if count == 0:
                state = ST_TITLE

print(cook_book)