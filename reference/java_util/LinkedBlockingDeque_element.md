#### element

```
public E element()
```
Retrieves, but does not remove, the head of the queue represented by
this deque. This method differs from `peek` only in that
it throws an exception if this deque is empty.This method is equivalent to `getFirst`.
Specified by:
`element` in interface `BlockingDeque<E>`
Specified by:
`element` in interface `Deque<E>`
Specified by:
`element` in interface `Queue<E>`
Overrides:
`element` in class `AbstractQueue<E>`
Returns:
the head of the queue represented by this deque
Throws:
`NoSuchElementException` - if this deque is empty

