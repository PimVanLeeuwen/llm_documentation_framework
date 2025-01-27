#### take

```
public E take()
       throws InterruptedException
```
Description copied from interface: `BlockingDeque`
Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), waiting if
necessary until an element becomes available.This method is equivalent to `takeFirst`.
Specified by:
`take` in interface `BlockingDeque<E>`
Specified by:
`take` in interface `BlockingQueue<E>`
Returns:
the head of this deque
Throws:
`InterruptedException` - if interrupted while waiting

