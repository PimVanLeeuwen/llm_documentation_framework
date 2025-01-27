#### poll

```
E poll(long timeout,
       TimeUnit unit)
throws InterruptedException
```
Retrieves and removes the head of the queue represented by this deque
(in other words, the first element of this deque), waiting up to the
specified wait time if necessary for an element to become available.This method is equivalent to
`pollFirst`.
Specified by:
`poll` in interface `BlockingQueue<E>`
Parameters:
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
the head of this deque, or `null` if the
specified waiting time elapses before an element is available
Throws:
`InterruptedException` - if interrupted while waiting

