#### offerLast

```
public boolean offerLast(E e,
                         long timeout,
                         TimeUnit unit)
                  throws InterruptedException
```
Description copied from interface: `BlockingDeque`
Inserts the specified element at the end of this deque,
waiting up to the specified wait time if necessary for space to
become available.
Specified by:
`offerLast` in interface `BlockingDeque<E>`
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
`NullPointerException` - if the specified element is null
`InterruptedException` - if interrupted while waiting

