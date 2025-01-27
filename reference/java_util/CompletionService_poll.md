#### poll

```
Future<V> poll(long timeout,
               TimeUnit unit)
        throws InterruptedException
```
Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.
Parameters:
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
the Future representing the next completed task or
`null` if the specified waiting time elapses
before one is present
Throws:
`InterruptedException` - if interrupted while waiting




