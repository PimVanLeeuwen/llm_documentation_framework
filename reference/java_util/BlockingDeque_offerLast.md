#### offerLast

```
boolean offerLast(E e,
                  long timeout,
                  TimeUnit unit)
           throws InterruptedException
```
Inserts the specified element at the end of this deque,
waiting up to the specified wait time if necessary for space to
become available.
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
`ClassCastException` - if the class of the specified element
prevents it from being added to this deque
`NullPointerException` - if the specified element is null
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this deque

