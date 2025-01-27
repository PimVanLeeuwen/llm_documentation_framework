#### getSharedQueuedThreads

```
public final Collection<Thread> getSharedQueuedThreads()
```
Returns a collection containing threads that may be waiting to
acquire in shared mode. This has the same properties
as `getQueuedThreads()` except that it only returns
those threads waiting due to a shared acquire.
Returns:
the collection of threads

