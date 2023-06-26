null_dict = {
    None: 'Nothing: None',
    0: 'Zero: 0',  # noqa: F601
    '': 'Empty:',
    False: 'Fake: False',  # noqa: F601
}


def NULL_not_found(object: any) -> int:
    # Float NaN specific logic
    # https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
    if isinstance(object, float) and object != object:
        print(f'Cheese: nan {type(object)}')
        return 0
    if object in null_dict.keys():
        print(f'{null_dict[object]} {type(object)}')
        return 0
    print('Type not Found')
    return 1
