#### offer

```
public boolean offer(E e,
                     long timeout,
                     TimeUnit unit)
```
Inserts the specified element into this priority queue.
As the queue is unbounded, this method will never block or
return `false`.
Specified by:
`offer` in interface `BlockingQueue<E>`
Parameters:
`e` - the element to add
`timeout` - This parameter is ignored as the method never blocks
`unit` - This parameter is ignored as the method never blocks
Returns:
`true` (as specified by
`BlockingQueue.offer`)
Throws:
`ClassCastException` - if the specified element cannot be compared
with elements currently in the priority queue according to the
priority queue's ordering
`NullPointerException` - if the specified element is null

