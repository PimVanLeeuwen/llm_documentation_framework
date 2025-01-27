#### getWaitQueueLength

```
protected final int getWaitQueueLength()
```
Returns an estimate of the number of threads waiting on
this condition.
Implements `AbstractQueuedSynchronizer.getWaitQueueLength(ConditionObject)`.
Returns:
the estimated number of waiting threads
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`

