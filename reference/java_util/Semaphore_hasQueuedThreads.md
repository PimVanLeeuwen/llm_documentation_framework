#### hasQueuedThreads

```
public final boolean hasQueuedThreads()
```
Queries whether any threads are waiting to acquire. Note that
because cancellations may occur at any time, a `true`
return does not guarantee that any other thread will ever
acquire. This method is designed primarily for use in
monitoring of the system state.
Returns:
`true` if there may be other threads waiting to
acquire the lock

