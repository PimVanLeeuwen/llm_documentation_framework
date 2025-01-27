#### acquire

```
public final void acquire(long arg)
```
Acquires in exclusive mode, ignoring interrupts. Implemented
by invoking at least once `tryAcquire(long)`,
returning on success. Otherwise the thread is queued, possibly
repeatedly blocking and unblocking, invoking `tryAcquire(long)` until success. This method can be used
to implement method `Lock.lock()`.
Parameters:
`arg` - the acquire argument. This value is conveyed to
`tryAcquire(long)` but is otherwise uninterpreted and
can represent anything you like.

