#### put

```
public void put(E e)
         throws InterruptedException
```
Description copied from interface: `BlockingDeque`
Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque), waiting if necessary for
space to become available.This method is equivalent to `putLast`.
Specified by:
`put` in interface `BlockingDeque<E>`
Specified by:
`put` in interface `BlockingQueue<E>`
Parameters:
`e` - the element to add
Throws:
`NullPointerException` - if the specified element is null
`InterruptedException` - if interrupted while waiting

