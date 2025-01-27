#### poll

```
public E poll(long timeout,
              TimeUnit unit)
       throws InterruptedException
```
Retrieves and removes the head of this queue, waiting if necessary
until an element with an expired delay is available on this queue,
or the specified wait time expires.
Specified by:
`poll` in interface `BlockingQueue<E extends Delayed>`
Parameters:
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
the head of this queue, or `null` if the
specified waiting time elapses before an element with
an expired delay becomes available
Throws:
`InterruptedException` - if interrupted while waiting

