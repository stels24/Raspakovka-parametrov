# Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 6, b = 10, c = "Hello")
print_params(a = 3, b = "WWW")


def print_params(a = 1, b = 25, c = [1,2,3]):
    print(a, b, c)

print_params()

# Распаковка параметров:

def print_params(a, b, c):
    print(a, b, c)

values_list = {3, "DDD", False}
values_dict = {"a": 6, "b": False , "c": "Apll"}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:

def print_params(a, b):
    print(a, b)

values_list_2 = ('строка', 42)

print_params(*values_list_2)
