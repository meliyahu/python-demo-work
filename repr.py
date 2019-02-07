class String:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other


if __name__ == '__main__':
    string = String('Hello World')
    print(string)
    print(string + ', thank you for having me')
