#### getWaitingThreads

```
public final Collection<Thread> getWaitingThreads(AbstractQueuedSynchronizer.ConditionObject condition)
```
Returns a collection containing those threads that may be
waiting on the given condition associated with this
synchronizer. Because the actual set of threads may change
dynamically while constructing this result, the returned
collection is only a best-effort estimate. The elements of the
returned collection are in no particular order.
Parameters:
`condition` - the condition
Returns:
the collection of threads
Throws:
`IllegalMonitorStateException` - if exclusive synchronization
is not held
`IllegalArgumentException` - if the given condition is
not associated with this synchronizer
`NullPointerException` - if the condition is null




