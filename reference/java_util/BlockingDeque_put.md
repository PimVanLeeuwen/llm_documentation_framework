#### put

```
void put(E e)
  throws InterruptedException
```
Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque), waiting if necessary for
space to become available.This method is equivalent to `putLast`.
Specified by:
`put` in interface `BlockingQueue<E>`
Parameters:
`e` - the element to add
Throws:
`InterruptedException` - if interrupted while waiting
`ClassCastException` - if the class of the specified element
prevents it from being added to this deque
`NullPointerException` - if the specified element is null
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this deque

