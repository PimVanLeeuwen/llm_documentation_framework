#### signal

```
public final void signal()
```
Moves the longest-waiting thread, if one exists, from the
wait queue for this condition to the wait queue for the
owning lock.
Specified by:
`signal` in interface `Condition`
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`

