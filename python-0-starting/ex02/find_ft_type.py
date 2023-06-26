# 문제에서는 Object type을 출력하라고 되어있지만... int는 type이 없다 출력되서 의문임
# iterable한지 아닌지를 기준으로 구현함
# https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
def all_thing_is_obj(object: any) -> int:
    try:
        iter(object)
    except TypeError:
        print('Type not found')
    else:
        type_title = type(object).__name__.title()
        if type_title == 'Str':
            type_title = f'{object} is in the kitchen'
        print(f'{type_title} : {type(object)}')
    return 42
