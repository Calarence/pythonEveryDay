class Person:
    'an example to understand how property works'

    def __init__(self, first_name):

        self.first_name = first_name

    @property
    def first_name(self):
        'Getter function'
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        'Setter function'
        if not isinstance(value, str):
            raise TypeError("Expected a string")

        self._first_name = value

    @first_name.deleter
    def first_name(self):
        'Deleter function (optional)'
        raise AttributeError("Can't delete attribute")
