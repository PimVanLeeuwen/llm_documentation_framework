#### hasWaiters

```
protected final boolean hasWaiters()
```
Queries whether any threads are waiting on this condition.
Implements `AbstractQueuedLongSynchronizer.hasWaiters(ConditionObject)`.
Returns:
`true` if there are any waiting threads
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedLongSynchronizer.isHeldExclusively()`
returns `false`

