t_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
def all_thing_is_obj(item):
    
    return type(item)
print(all_thing_is_obj(t_list))
print(all_thing_is_obj(ft_tuple))
print(all_thing_is_obj(ft_set))
print(all_thing_is_obj(ft_dict))
print(all_thing_is_obj("Brian"))
print(all_thing_is_obj("Toto"))
print(all_thing_is_obj(10))
