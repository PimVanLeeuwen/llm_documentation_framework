#### awaitUntil

```
public final boolean awaitUntil(Date deadline)
                         throws InterruptedException
```
Implements absolute timed condition wait.If current thread is interrupted, throw InterruptedException.Save lock state returned by `AbstractQueuedLongSynchronizer.getState()`.Invoke `AbstractQueuedLongSynchronizer.release(long)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled, interrupted, or timed out.Reacquire by invoking specialized version of
`AbstractQueuedLongSynchronizer.acquire(long)` with saved state as argument.If interrupted while blocked in step 4, throw InterruptedException.If timed out while blocked in step 4, return false, else true.
Specified by:
`awaitUntil` in interface `Condition`
Parameters:
`deadline` - the absolute time to wait until
Returns:
`false` if the deadline has elapsed upon return, else
`true`
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

