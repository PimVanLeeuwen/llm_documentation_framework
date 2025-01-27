#### acquireShared

```
public final void acquireShared(int arg)
```
Acquires in shared mode, ignoring interrupts. Implemented by
first invoking at least once `tryAcquireShared(int)`,
returning on success. Otherwise the thread is queued, possibly
repeatedly blocking and unblocking, invoking `tryAcquireShared(int)` until success.
Parameters:
`arg` - the acquire argument. This value is conveyed to
`tryAcquireShared(int)` but is otherwise uninterpreted
and can represent anything you like.

