#### acquire

```
public final void acquire(int arg)
```
Acquires in exclusive mode, ignoring interrupts. Implemented
by invoking at least once `tryAcquire(int)`,
returning on success. Otherwise the thread is queued, possibly
repeatedly blocking and unblocking, invoking `tryAcquire(int)` until success. This method can be used
to implement method `Lock.lock()`.
Parameters:
`arg` - the acquire argument. This value is conveyed to
`tryAcquire(int)` but is otherwise uninterpreted and
can represent anything you like.

