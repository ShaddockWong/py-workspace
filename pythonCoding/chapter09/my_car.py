# from car import Car

# my_new_car = Car("audi", "a4", 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# # 从一个模块中导入多个类
# from car import Car, ElectricCar

# my_mustang = Car("ford", "mustang", 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar("nissan", "leaf", 2024)
# print(my_leaf.get_descriptive_name())

# 导入整个模块
import car

my_mustang = car.Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
