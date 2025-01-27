#### pollFirst

```
public E pollFirst(long timeout,
                   TimeUnit unit)
            throws InterruptedException
```
Description copied from interface: `BlockingDeque`
Retrieves and removes the first element of this deque, waiting
up to the specified wait time if necessary for an element to
become available.
Specified by:
`pollFirst` in interface `BlockingDeque<E>`
Parameters:
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
the head of this deque, or `null` if the specified
waiting time elapses before an element is available
Throws:
`InterruptedException` - if interrupted while waiting

