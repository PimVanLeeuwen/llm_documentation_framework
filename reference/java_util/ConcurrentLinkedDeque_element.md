#### element

```
public E element()
```
Description copied from interface: `Deque`
Retrieves, but does not remove, the head of the queue represented by
this deque (in other words, the first element of this deque).
This method differs from `peek` only in that it throws an
exception if this deque is empty.This method is equivalent to `Deque.getFirst()`.
Specified by:
`element` in interface `Deque<E>`
Specified by:
`element` in interface `Queue<E>`
Returns:
the head of the queue represented by this deque
Throws:
`NoSuchElementException` - if this deque is empty

