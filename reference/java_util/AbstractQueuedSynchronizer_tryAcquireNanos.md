#### tryAcquireNanos

```
public final boolean tryAcquireNanos(int arg,
                                     long nanosTimeout)
                              throws InterruptedException
```
Attempts to acquire in exclusive mode, aborting if interrupted,
and failing if the given timeout elapses. Implemented by first
checking interrupt status, then invoking at least once `tryAcquire(int)`, returning on success. Otherwise, the thread is
queued, possibly repeatedly blocking and unblocking, invoking
`tryAcquire(int)` until success or the thread is interrupted
or the timeout elapses. This method can be used to implement
method `Lock.tryLock(long, TimeUnit)`.
Parameters:
`arg` - the acquire argument. This value is conveyed to
`tryAcquire(int)` but is otherwise uninterpreted and
can represent anything you like.
`nanosTimeout` - the maximum number of nanoseconds to wait
Returns:
`true` if acquired; `false` if timed out
Throws:
`InterruptedException` - if the current thread is interrupted

