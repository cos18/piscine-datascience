from new_student import Student


def test():
    """Test function
    """
    student = Student(name='Edward', surname='agle')
    print(student)

    try:
        wrong = Student(name='Edward', surname='agle', id='wrong')
        print(wrong)
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == '__main__':
    test()
