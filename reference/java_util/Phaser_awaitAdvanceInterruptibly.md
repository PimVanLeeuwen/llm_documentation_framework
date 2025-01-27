#### awaitAdvanceInterruptibly

```
public int awaitAdvanceInterruptibly(int phase,
                                     long timeout,
                                     TimeUnit unit)
                              throws InterruptedException,
                                     TimeoutException
```
Awaits the phase of this phaser to advance from the given phase
value or the given timeout to elapse, throwing `InterruptedException` if interrupted while waiting, or
returning immediately if the current phase is not equal to the
given phase value or this phaser is terminated.
Parameters:
`phase` - an arrival phase number, or negative value if
terminated; this argument is normally the value returned by a
previous call to `arrive` or `arriveAndDeregister`.
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
the next arrival phase number, or the argument if it is
negative, or the (negative) current phase
if terminated
Throws:
`InterruptedException` - if thread interrupted while waiting
`TimeoutException` - if timed out while waiting

