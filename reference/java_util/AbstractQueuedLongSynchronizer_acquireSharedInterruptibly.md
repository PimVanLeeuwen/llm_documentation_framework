#### acquireSharedInterruptibly

```
public final void acquireSharedInterruptibly(long arg)
                                      throws InterruptedException
```
Acquires in shared mode, aborting if interrupted. Implemented
by first checking interrupt status, then invoking at least once
`tryAcquireShared(long)`, returning on success. Otherwise the
thread is queued, possibly repeatedly blocking and unblocking,
invoking `tryAcquireShared(long)` until success or the thread
is interrupted.
Parameters:
`arg` - the acquire argument.
This value is conveyed to `tryAcquireShared(long)` but is
otherwise uninterpreted and can represent anything
you like.
Throws:
`InterruptedException` - if the current thread is interrupted

