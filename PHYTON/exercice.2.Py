# find_ft_type.py

def all_thing_is_obj(obj: any) -> int:
    # Print the object type
    if isinstance(obj, list):
        print("List :", type(obj))
    elif isinstance(obj, tuple):
        print("Tuple :", type(obj))
    elif isinstance(obj, set):
        print("Set :", type(obj))
    elif isinstance(obj, dict):
        print("Dict :", type(obj))
    elif isinstance(obj, str):
        print(obj, "is in the kitchen :", type(obj))
    else:
        print("Type not found")

    # Return 42
    return 42
# tester.py

from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

