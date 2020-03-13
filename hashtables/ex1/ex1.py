#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # for index, find length and insert into hashtable
    for idx in range(0, length):
        hash_table_insert(ht, weights[idx], idx)
    # second loop not nested avoids quadratic runtime
    for idx in range(0, length):
        answer = hash_table_retrieve(ht, limit - weights[idx])
    # if hash table contains an entry for limit - weight:
        if answer:
    # taking data from hashtable and returning
    # weights sum to limit
            return max(idx, answer), min(idx, answer)
    # if key doesn't exist, or if indices don't fit in correct index
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
