#### acquireSharedInterruptibly

```
public final void acquireSharedInterruptibly(int arg)
                                      throws InterruptedException
```
Acquires in shared mode, aborting if interrupted. Implemented
by first checking interrupt status, then invoking at least once
`tryAcquireShared(int)`, returning on success. Otherwise the
thread is queued, possibly repeatedly blocking and unblocking,
invoking `tryAcquireShared(int)` until success or the thread
is interrupted.
Parameters:
`arg` - the acquire argument.
This value is conveyed to `tryAcquireShared(int)` but is
otherwise uninterpreted and can represent anything
you like.
Throws:
`InterruptedException` - if the current thread is interrupted

