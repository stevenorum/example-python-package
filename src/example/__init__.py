#!/usr/bin/env python

def example_function(*args, **kwargs):
    print("You just called example_function!")

class ExampleObject(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print("You just initialized an ExampleObject!")
