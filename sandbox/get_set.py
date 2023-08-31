# https://elfi-y.medium.com/python-descriptor-a-thorough-guide-60a915f67aa9
# https://docs.python.org/3/howto/descriptor.html

class R:

    def __init__(self, register_address: int) -> None:
        self.register = register_address


    # __get__(self, instance, owner)
    # __get__(self, obj, objtype=None):
    def __get__(self, obj, objtype=None):
        print("__get__", obj, objtype, obj._address)  # __get__ <__main__.A object at 0x7f629e95ba90> <class '__main__.A'> 24
        return 1

    def __set__(self, obj, value):
        print("__set__", obj, value)


class A:
    _device_id = R(0x0f)

    def __init__(self, address=0x18):
        self._address = address

        i = self._device_id
        print("i", i)


a = A()
