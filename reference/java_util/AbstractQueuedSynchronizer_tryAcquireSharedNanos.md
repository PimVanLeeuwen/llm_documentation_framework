#### tryAcquireSharedNanos

```
public final boolean tryAcquireSharedNanos(int arg,
                                           long nanosTimeout)
                                    throws InterruptedException
```
Attempts to acquire in shared mode, aborting if interrupted, and
failing if the given timeout elapses. Implemented by first
checking interrupt status, then invoking at least once `tryAcquireShared(int)`, returning on success. Otherwise, the
thread is queued, possibly repeatedly blocking and unblocking,
invoking `tryAcquireShared(int)` until success or the thread
is interrupted or the timeout elapses.
Parameters:
`arg` - the acquire argument. This value is conveyed to
`tryAcquireShared(int)` but is otherwise uninterpreted
and can represent anything you like.
`nanosTimeout` - the maximum number of nanoseconds to wait
Returns:
`true` if acquired; `false` if timed out
Throws:
`InterruptedException` - if the current thread is interrupted

