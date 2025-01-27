#### offer

```
public boolean offer(E e,
                     long timeout,
                     TimeUnit unit)
              throws InterruptedException
```
Inserts the specified element at the tail of this queue, waiting
up to the specified wait time for space to become available if
the queue is full.
Specified by:
`offer` in interface `BlockingQueue<E>`
Parameters:
`e` - the element to add
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
`true` if successful, or `false` if
the specified waiting time elapses before space is available
Throws:
`InterruptedException` - if interrupted while waiting
`NullPointerException` - if the specified element is null

