# -*- coding: utf-8 -*-

class Counter:

    def __init__(self, start_value=0):
        # counter always has to start at 0
        if start_value > 0:
            self._count = start_value
        else:
            self._count = 0

    def increment(self):
        self._count += 1
        return self._count

    def decrement(self):
        # counter cannot go below 0
        if self._count - 1 < 0:
            self._count = 0
        else:
            self._count -= 1
        return self._count


class Namer:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "[ {} ]: name={} age={}".format(
            self.__class__,
            self._name,
            self._age,
        )

    def say_my_name(self):
        # NOTE: this calls the __str__ override method
        print(self)

    def countdown(self):
        age_counter = Counter(start_value=self._age)
        next_age = age_counter._count
        while next_age > 0:
            print(next_age)
            next_age = age_counter.decrement()
        print("[ DONE ]")

    def show_me_my_data_guts(self):
        #
        # A Python class is just a fancy wrapper
        # around a dictionary. It has special ways to access
        # the dictionary internally from the class. So we can
        # do things such as this to get an internal view of the class
        #
        return "{}".format(self.__dict__)
