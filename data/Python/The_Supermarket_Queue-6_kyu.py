# https://www.codewars.com/kata/57b06f90e298a7b53d000a86
# 2023-03-24T08:18:21.929+0000
def queue_time(customers, n):
    # If there are no customers, return 0
    if len(customers) == 0:
        return 0

    # If there's less customers than tills return the highest time
    if len(customers) <= n:
        return max(customers)

    # Time
    time = 0

    # Now let's simulate people going through the queue
    # Fill the tills
    tills = [customers.pop(0) for i in range(n)]

    while len(customers) > 0:
        # Find the till with the shortest queue
        shortest = min(tills)
        # Find the index of the shortest queue
        index = tills.index(shortest)
        # Remove the customer from the till and adjust all the other tills
        tills = [till - shortest for till in tills]
        time += shortest

        # Now add customers to any empty tills
        tills = [customers.pop(0) if till <= 0 and customers else till for till in tills]

    # We've popped all the customers so now we just need to wait for the tills to empty
    time += max(tills)

    return time
