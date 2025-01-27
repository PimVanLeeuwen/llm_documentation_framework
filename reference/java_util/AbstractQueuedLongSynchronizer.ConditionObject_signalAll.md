#### signalAll

```
public final void signalAll()
```
Moves all threads from the wait queue for this condition to
the wait queue for the owning lock.
Specified by:
`signalAll` in interface `Condition`
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedLongSynchronizer.isHeldExclusively()`
returns `false`

