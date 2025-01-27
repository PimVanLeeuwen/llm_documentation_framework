#### getWaitingThreads

```
protected final Collection<Thread> getWaitingThreads()
```
Returns a collection containing those threads that may be
waiting on this Condition.
Implements `AbstractQueuedSynchronizer.getWaitingThreads(ConditionObject)`.
Returns:
the collection of threads
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`




