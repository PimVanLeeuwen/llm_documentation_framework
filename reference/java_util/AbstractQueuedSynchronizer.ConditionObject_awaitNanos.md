#### awaitNanos

```
public final long awaitNanos(long nanosTimeout)
                      throws InterruptedException
```
Implements timed condition wait.If current thread is interrupted, throw InterruptedException.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled, interrupted, or timed out.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.If interrupted while blocked in step 4, throw InterruptedException.
Specified by:
`awaitNanos` in interface `Condition`
Parameters:
`nanosTimeout` - the maximum time to wait, in nanoseconds
Returns:
an estimate of the `nanosTimeout` value minus
the time spent waiting upon return from this method.
A positive value may be used as the argument to a
subsequent call to this method to finish waiting out
the desired time. A value less than or equal to zero
indicates that no time remains.
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

