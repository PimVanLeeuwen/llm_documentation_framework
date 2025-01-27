#### hasWaiters

```
public final boolean hasWaiters(AbstractQueuedSynchronizer.ConditionObject condition)
```
Queries whether any threads are waiting on the given condition
associated with this synchronizer. Note that because timeouts
and interrupts may occur at any time, a `true` return
does not guarantee that a future `signal` will awaken
any threads. This method is designed primarily for use in
monitoring of the system state.
Parameters:
`condition` - the condition
Returns:
`true` if there are any waiting threads
Throws:
`IllegalMonitorStateException` - if exclusive synchronization
is not held
`IllegalArgumentException` - if the given condition is
not associated with this synchronizer
`NullPointerException` - if the condition is null

