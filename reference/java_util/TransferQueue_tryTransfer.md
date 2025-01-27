#### tryTransfer

```
boolean tryTransfer(E e,
                    long timeout,
                    TimeUnit unit)
             throws InterruptedException
```
Transfers the element to a consumer if it is possible to do so
before the timeout elapses.More precisely, transfers the specified element immediately
if there exists a consumer already waiting to receive it (in
`BlockingQueue.take()` or timed `poll`),
else waits until the element is received by a consumer,
returning `false` if the specified wait time elapses
before the element can be transferred.
Parameters:
`e` - the element to transfer
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
`true` if successful, or `false` if
the specified waiting time elapses before completion,
in which case the element is not left enqueued
Throws:
`InterruptedException` - if interrupted while waiting,
in which case the element is not left enqueued
`ClassCastException` - if the class of the specified element
prevents it from being added to this queue
`NullPointerException` - if the specified element is null
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this queue

