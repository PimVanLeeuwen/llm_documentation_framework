#### getExclusiveQueuedThreads

```
public final Collection<Thread> getExclusiveQueuedThreads()
```
Returns a collection containing threads that may be waiting to
acquire in exclusive mode. This has the same properties
as `getQueuedThreads()` except that it only returns
those threads waiting due to an exclusive acquire.
Returns:
the collection of threads

