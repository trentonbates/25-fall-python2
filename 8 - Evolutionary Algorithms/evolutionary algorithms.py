from items import items
from random import sample

def total(list, value=False):
    total = 0
    for item in list:
        if value:
            total += item[1]
        else:
            total += item[0]
    return total

def knapsack(capacity):
    # INITIALIZE
    idk = list()
    best_value = 0
    prev_best = 0
    generation = 1

    while True:

        for offspring in range(100):

            # MUTATE
            random_index = items.index(sample(items, 1)[0])
            item = items[random_index]

            while total(idk) + item[0] > capacity:
                random_index = idk.index(sample(idk, 1)[0])
                idk.remove(idk[random_index])

            idk.append(item)

            # SELECT
            offspring_value = total(idk, True)
            
            if offspring_value > best_value:
                best_value = offspring_value

        # TERMINATE
        if best_value == prev_best:
            return
        
        print(f'Generation {generation}: Value {best_value}')
        prev_best = best_value
        generation += 1

knapsack(300)