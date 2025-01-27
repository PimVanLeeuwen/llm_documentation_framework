#### await

```
public final boolean await(long time,
                           TimeUnit unit)
                    throws InterruptedException
```
Implements timed condition wait.If current thread is interrupted, throw InterruptedException.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled, interrupted, or timed out.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.If interrupted while blocked in step 4, throw InterruptedException.If timed out while blocked in step 4, return false, else true.
Specified by:
`await` in interface `Condition`
Parameters:
`time` - the maximum time to wait
`unit` - the time unit of the `time` argument
Returns:
`false` if the waiting time detectably elapsed
before return from the method, else `true`
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

