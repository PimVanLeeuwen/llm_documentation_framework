#### poll

```
E poll(long timeout,
       TimeUnit unit)
throws InterruptedException
```
Retrieves and removes the head of this queue, waiting up to the
specified wait time if necessary for an element to become available.
Parameters:
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
the head of this queue, or `null` if the
specified waiting time elapses before an element is available
Throws:
`InterruptedException` - if interrupted while waiting

