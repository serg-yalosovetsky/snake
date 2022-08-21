import random


h = 20
w = 20

fruit_symbol = 'S'
field_symbol = 'x'
snake_symbol = 'o'
snake_head_symbol = 'Q'
snake = []

field = []

def gen_field(h, w, field_symbol='x'):
    row = []
    field = []
    for _ in range(w):
        row.append(field_symbol)
    for _ in range(h):
        field.append(row.copy())
    
    free = []
    for i in range(w):
        for j in range(h):
            field[i][j] = field_symbol
            free.append((i,j))        

    return field, free

def print_snake(field):
    for row in field:
        for e in row:
            print(e, end='')
            print(' ', end='')
        print()

def gen_fruit(fruit, field, snake_fields):
    free_field = []
    for i in range(w):
        for j in range(h):
            if (i,j) not in snake_fields:
                free_field.append((i,j))       

    len_field = len(free_field)
    fruit_pozition = random.randint(0, len_field-1)
    address_fruit = free_field[fruit_pozition]
    field[address_fruit[0]][address_fruit[1]] = fruit
    return field


def gen_snake(snake, snake_head, field):
    snake_x_0_poz = random.randint(0, w - 1)
    snake_y_0_poz = random.randint(0, h - 1)
    print(f'head, {snake_x_0_poz} , {snake_y_0_poz}')
    where_snake_tail = [
        [snake_x_0_poz-1, snake_y_0_poz],
        [snake_x_0_poz+1, snake_y_0_poz],
        [snake_x_0_poz, snake_y_0_poz-1],
        [snake_x_0_poz, snake_y_0_poz+1],
    ]
    print(f'tail vars, {where_snake_tail}')

    for index, item in enumerate(where_snake_tail.copy()):
        if item[0] < 0 or item[0] >= w or item[1] < 0 or item[1] >= h:
            where_snake_tail.pop(index)
    snake_tail_pozition = random.randint(0, len(where_snake_tail) - 1)
    print(f'tail random var {snake_tail_pozition}')
    where_snake_tail_elem = where_snake_tail[snake_tail_pozition]
    print(f'tail random poz {where_snake_tail_elem}')


    field[snake_x_0_poz][snake_y_0_poz] = snake_head
    field[where_snake_tail_elem[0]][where_snake_tail_elem[1]] = snake
    snake_array = [
                    [snake_x_0_poz, snake_y_0_poz], 
                    [where_snake_tail_elem[0], where_snake_tail_elem[1]],
                    ]
    snake_head_poz = (snake_x_0_poz, snake_y_0_poz)

    return field, snake_array, snake_head_poz 


field, free_field = gen_field(h,w)

print_snake(field)

field = gen_fruit(fruit=fruit_symbol, field=field, snake_fields=snake)

print_snake(field)

field, snake, snake_head = gen_snake(snake=snake_symbol, snake_head=snake_head_symbol, field=field)

print_snake(field)
