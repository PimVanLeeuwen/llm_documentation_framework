#### acquireInterruptibly

```
public final void acquireInterruptibly(int arg)
                                throws InterruptedException
```
Acquires in exclusive mode, aborting if interrupted.
Implemented by first checking interrupt status, then invoking
at least once `tryAcquire(int)`, returning on
success. Otherwise the thread is queued, possibly repeatedly
blocking and unblocking, invoking `tryAcquire(int)`
until success or the thread is interrupted. This method can be
used to implement method `Lock.lockInterruptibly()`.
Parameters:
`arg` - the acquire argument. This value is conveyed to
`tryAcquire(int)` but is otherwise uninterpreted and
can represent anything you like.
Throws:
`InterruptedException` - if the current thread is interrupted

