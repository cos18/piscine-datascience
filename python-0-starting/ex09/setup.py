from setuptools import setup, find_packages


def main():
    """
    Setting function to make package
    poetry run python setup.py sdist bdist_wheel
    poetry run pip install ./dist/ft_package-0.0.1-py3-none-any.whl
    """
    setup(
        name='ft_package',
        version='0.0.1',
        description='A sample test package',
        url='https://github.com/cos18/piscine-datascience',
        author='sunpark',
        author_email='sunpark@student.42seoul.kr',
        license='MIT',
        python_requires='>=3',
        packages=find_packages(exclude=[]),
    )


if __name__ == "__main__":
    main()
