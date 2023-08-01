import modules
from modules import pi


result = modules.add(5, 3)
print(result)
print(modules.add(5, 3))


result = modules.add(10, 3)
print(result)

result = modules.multiply(45, 2)
print(result)

print(modules.pi)


def area():
    return modules.pi * modules.pi


print(area())
