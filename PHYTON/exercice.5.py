def count_in_list(lst, item):
   
    return lst.count(item)


from time import sleep

import tqdm

from Loading import ft_tqdm


print("Testing ft_tqdm:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

print("Testing tqdm:")
for elem in tqdm(range(333)):
    sleep(0.005)
print()


