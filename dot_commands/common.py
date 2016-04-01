# -*- coding: utf-8 -*-

def dictKeyInArray(key, value, array):
    for index, item in enumerate(array):
        if item[key] == value:
            return index

    return -1


def importModule(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod
