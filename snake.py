import random
from typing import List, Tuple

class snake:
        
    h = 20
    w = 20
    auto_gen_fruit = True
    fruit_symbol = 'S'
    field_symbol = 'x'
    snake_symbol = 'o'
    snake_head_symbol = 'Q'
    collision_symbol = 'Z'
    snake = []

    field = []

    @classmethod
    def gen_field(cls):
        row = []
        field = []
        for _ in range(cls.w):
            row.append(cls.field_symbol)
        for _ in range(cls.h):
            field.append(row.copy())
        
        free = []
        for i in range(cls.w):
            for j in range(cls.h):
                field[i][j] = cls.field_symbol
                free.append((i,j))        

        return field, free

    @classmethod
    def print_snake(cls, field: List):
        for row in field:
            for e in row:
                print(e, end='')
                print(' ', end='')
            print()

    @classmethod
    def gen_fruit(cls, field: List, snake_fields: List):
        free_field = []
        for i in range(cls.w):
            for j in range(cls.h):
                if (i,j) not in snake_fields:
                    free_field.append((i,j))       

        len_field = len(free_field)
        fruit_pozition = random.randint(0, len_field-1)
        address_fruit = free_field[fruit_pozition]
        field[address_fruit[0]][address_fruit[1]] = cls.fruit_symbol
        return field

    @classmethod
    def check_snake_in_field(cls, x: int, y: int):
        if ((x < cls.w and x >= 0) and (y < cls.h and y >= 0)):
            return True
        return False

    @classmethod
    def gen_snake(cls, field: List):
        snake_x_0_poz = random.randint(0, cls.w - 1)
        snake_y_0_poz = random.randint(0, cls.h - 1)
        print(f'head, {snake_x_0_poz} , {snake_y_0_poz}')
        where_snake_tail = [
            [snake_x_0_poz-1, snake_y_0_poz],
            [snake_x_0_poz+1, snake_y_0_poz],
            [snake_x_0_poz, snake_y_0_poz-1],
            [snake_x_0_poz, snake_y_0_poz+1],
        ]
        print(f'tail vars, {where_snake_tail}')

        for index, item in enumerate(where_snake_tail.copy()):
            # if item[0] < 0 or item[0] >= cls.w or item[1] < 0 or item[1] >= cls.h:
            if cls.check_snake_in_field(*item):
                where_snake_tail.pop(index)
        snake_tail_pozition = random.randint(0, len(where_snake_tail) - 1)
        print(f'tail random var {snake_tail_pozition}')
        where_snake_tail_elem = where_snake_tail[snake_tail_pozition]
        print(f'tail random poz {where_snake_tail_elem}')


        field[snake_x_0_poz][snake_y_0_poz] = cls.snake_head_symbol
        field[where_snake_tail_elem[0]][where_snake_tail_elem[1]] = cls.snake_symbol
        snake_array = [
                        (snake_x_0_poz, snake_y_0_poz), 
                        (where_snake_tail_elem[0], where_snake_tail_elem[1]),
                        ]
        snake_head_poz = (snake_x_0_poz, snake_y_0_poz)

        return field, snake_array, snake_head_poz 

    @classmethod
    def move_snake(cls, snake: List, snake_head: Tuple, field: List, move: Tuple):
        '''
        return status of move, then field, than result snake and then snake head
        '''

        snake_eat = 'no eat'
        match move:
            case "up":
                move_vector = (-1, 0)
            case "down":
                move_vector = (1, 0)  
            case "right":
                move_vector = (0, 1)  
            case "left":
                move_vector = (0, -1)  
            case _:
                return 'wrong_params', field, snake, snake_head
        snake_new_head = (snake_head[0] + move_vector[0], snake_head[1] + move_vector[1])
        if snake_new_head == snake[-2]:
            print('snake cannot turn to 180 degree')
            return 'wrong_params', field, snake, snake_head

        if cls.check_snake_in_field(*snake_new_head):
            # first we check if snake eat a fruit
            # then we check if snake is in collision with itself
            # because we need to understand if we need cut tail of snake, or not 

            if field[snake_new_head[0]][snake_new_head[1]] == cls.fruit_symbol:
                print('snake eat fruit')
                snake_eat = 'eat'
                if cls.auto_gen_fruit:
                    field = cls.gen_fruit(field=field, snake_fields=snake_array)
                    
            else:
                tail = snake.pop(0)
                field[tail[0]][tail[1]] = cls.field_symbol
            if field[snake_new_head[0]][snake_new_head[1]] in snake:
                print('snake don`t uroboros')
                # snake lose
                field[snake_head[0]][snake_head[1]] = cls.collision_symbol
                return False, field, snake, snake_head      

           
            field[snake_new_head[0]][snake_new_head[1]] = cls.snake_head_symbol
            field[snake_head[0]][snake_head[1]] = cls.snake_symbol

            snake.append(snake_new_head)
            if snake_eat == 'eat' and cls.auto_gen_fruit:
                field = cls.gen_fruit(field=field, snake_fields=snake_array)
            return snake_eat, field, snake, snake_new_head
        else:
            field[snake_head[0]][snake_head[1]] = cls.collision_symbol
            # snake lose
            return False, field, snake, snake_head


field, free_field = snake.gen_field()

snake.print_snake(field)

field, snake_array, snake_head = snake.gen_snake(field=field)

snake.print_snake(field)

field = snake.gen_fruit(field=field, snake_fields=snake_array)

snake.print_snake(field)

status, field, snake_array, snake_head = snake.move_snake(snake=snake_array, snake_head=snake_head, field=field, move='up')
status, field, snake_array, snake_head = snake.move_snake(snake=snake_array, snake_head=snake_head, field=field, move='right')

print(snake_array)
print(snake_head)

snake.print_snake(field)
