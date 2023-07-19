null_dict = {
    None: 'Nothing: None',
    '': 'Empty:',
}


def NULL_not_found(object: any) -> int:
    # Float NaN specific logic
    # https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
    if type(object) == float and object != object:
        print('Cheese: nan ', end='')
    elif type(object) == int and object == 0:
        print('Zero: 0 ', end='')
    elif type(object) == bool and object is False:
        print('Fake: False ', end='')
    elif object in null_dict.keys():
        print(f'{null_dict[object]} ', end='')
    else:
        print('Type not Found')
        return 1
    print(type(object))
    return 0
