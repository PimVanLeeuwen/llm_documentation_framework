#### acquireShared

```
public final void acquireShared(long arg)
```
Acquires in shared mode, ignoring interrupts. Implemented by
first invoking at least once `tryAcquireShared(long)`,
returning on success. Otherwise the thread is queued, possibly
repeatedly blocking and unblocking, invoking `tryAcquireShared(long)` until success.
Parameters:
`arg` - the acquire argument. This value is conveyed to
`tryAcquireShared(long)` but is otherwise uninterpreted
and can represent anything you like.

