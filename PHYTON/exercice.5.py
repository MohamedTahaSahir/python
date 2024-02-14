

def count_in_list(lst, item):
    """
    Count the occurrences of an item in a list.

    Args:
        lst (list): The list to search.
        item: The item to count.

    Returns:
        int: The number of occurrences of the item in the list.
    """
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

