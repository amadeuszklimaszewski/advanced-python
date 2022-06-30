"""
Prototype Method aims to reduce the number of classes used for an
application. It allows you to copy existing objects independent of the
concrete implementation of their classes. Generally, here the object
is created by copying a prototypical instance during run-time.

It is highly recommended to use Prototype Method when the object creation
is an expensive task in terms of time and usage of resources and already
there exists a similar object. This method provides a way to copy the
original object and then modify it according to our needs.
"""

import copy


class Prototype:

    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value


class Type1(Prototype):
    def __init__(self, number):
        self._type = "Type1"
        self._value = number

    def clone(self):
        return copy.copy(self)


class Type2(Prototype):
    def __init__(self, number):
        self._type = "Type2"
        self._value = number

    def clone(self):
        return copy.copy(self)


class ObjectFactory:
    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        ObjectFactory.__type1Value1 = Type1(1)
        ObjectFactory.__type1Value2 = Type1(2)
        ObjectFactory.__type2Value1 = Type2(1)
        ObjectFactory.__type2Value2 = Type2(2)

    @staticmethod
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def getType1Value2():
        return ObjectFactory.__type1Value2.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()

    @staticmethod
    def getType2Value2():
        return ObjectFactory.__type2Value2.clone()


def main():
    ObjectFactory.initialize()

    instance = ObjectFactory.getType1Value1()
    print("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.getType1Value2()
    print("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.getType2Value1()
    print("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.getType2Value2()
    print("%s: %s" % (instance.getType(), instance.getValue()))


if __name__ == "__main__":
    main()
