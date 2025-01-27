#### getWaitingThreads

```
protected final Collection<Thread> getWaitingThreads()
```
Returns a collection containing those threads that may be
waiting on this Condition.
Implements `AbstractQueuedLongSynchronizer.getWaitingThreads(ConditionObject)`.
Returns:
the collection of threads
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedLongSynchronizer.isHeldExclusively()`
returns `false`




