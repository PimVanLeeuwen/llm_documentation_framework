#### poll

```
public Future<V> poll(long timeout,
                      TimeUnit unit)
               throws InterruptedException
```
Description copied from interface: `CompletionService`
Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.
Specified by:
`poll` in interface `CompletionService<V>`
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




