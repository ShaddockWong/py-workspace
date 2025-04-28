# def describe_pet(animal_type, pet_name):
#     """显式宠物的信息"""
#     print(f"\nI hava a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# # describe_pet("hamster", "harry")
# # describe_pet("dog", "willie")

# # 关键字实参
# describe_pet(animal_type="hamster", pet_name="harry")
# describe_pet(pet_name="harry", animal_type="hamster")


# 默认值
def describe_pet(pet_name, animal_type="dog"):
    """显式宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name="willie")
describe_pet("harry", "hamster")
