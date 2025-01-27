#### offer

```
public boolean offer(E e,
                     long timeout,
                     TimeUnit unit)
              throws InterruptedException
```
Description copied from interface: `BlockingDeque`
Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque), waiting up to the
specified wait time if necessary for space to become available.This method is equivalent to
`offerLast`.
Specified by:
`offer` in interface `BlockingDeque<E>`
Specified by:
`offer` in interface `BlockingQueue<E>`
Parameters:
`e` - the element to add
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
`true` if the element was added to this deque, else
`false`
Throws:
`NullPointerException` - if the specified element is null
`InterruptedException` - if interrupted while waiting

