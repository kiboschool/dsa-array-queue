# Array Queue

In this practice, you will implement the queue ADT using an array (Python list).

## Starter Code

You are given the file `arrayqueue.py`, which includes a skeleton implementation of the `ArrayQueue` class. This class implements the queue ADT and therefore holds stubs for the following methods:

* `enqueue()`: add an item at the rear of the queue
* `dequeue()`: remove the item at the front of the queue
* `front()`: get the item at the front of the queue, but don't remove it
* `is_empty()`: test if the queue is empty
* `is_full()`: test if the queue is full

***You should not change any of the existing methods in the `ArrayQueue` class.***

## Approach

To implement the queue using an array, you will implement a *circular queue* -- using all positions of the underlying Python list to represent the queue, and *wrapping around* the end of the Python list when necessary.

For example, say that an initially empty queue is created of length 5:

```text
[ None, None, None, None, None ]
```

And then we enqueue five items:

```text
[ 1, 2, 3, 4, 5 ]
  ^           ^
front        rear
```

If we dequeue two items, the state of the queue will look like:

```text
[ None, None, 3, 4, 5 ]
              ^     ^
           front   rear
```

If we want to then enqueue a sixth item, we need to *wrap around* to the front of the Python list and add the item in position 0. This will become the new rear of the queue:

```text
[ 6, None, 3, 4, 5 ]
  ^        ^
 rear    front
```

Both the front and rear indexes of the queue can wrap around to the beginning as needed. Doing so avoids the need to ever need to shift items in the array, keeping both `enqueue()` and `dequeue()` `O(1)` operations!

## Steps to Complete

Your task is to implement the methods of the queue ADT in the `ArrayQueue` class.

Start with the three easiest methods first:

1. `is_empty()`

    The `is_empty()` method should return whether the queue is empty. For this task, you should consult the value of `self.num_items`.

2. `is_full()`

    The `is_full()` method should return whether the queue is full. For this task, you should consult the value of the variables `self.num_items` and `self.max_items`.

3. `front()`

    The `front()` method should return the item at the front of the queue, but should *not* actually remove the item.

Once those methods are done, you can move on to the two slightly harder methods:

4. `enqueue()`

    The `enqueue()` method should first check whether the queue is full, and if it is, return `False` and do not enqueue the item.

    Otherwise, `enqueue()` should advance `self.rear_idx` to the next position, add the item to the new rear of the queue, and increment the number of items before returning `True`.

    Notes:

    * The `self.rear_idx` variable is initialized to -1 in the constructor so that it is set up correctly for the first call to `enqueue()` (which should advance `self.rear_idx` to 0 before filling it).
    * Since the rear index can wrap around to the beginning of the array, you need to account for this when advancing `self.rear_idx` to the next position.

5. `dequeue()`

    The `dequeue()` method should first check whether the queue is empty, and if it is, return `None`.

    Otherwise, `dequeue()` should save the item currently at the front of the queue, advance `self.front_idx` to the next position, and decrement the number of items before returning the saved item.

    Similar to `enqueue()`, it's possible for `self.front_idx` to need to wrap around to the front of the list.

## Testing

In `test_arrayqueue.py`, there are unit tests that cover each of the five methods described above.
