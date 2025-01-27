#### awaitUninterruptibly

```
public final void awaitUninterruptibly()
```
Implements uninterruptible condition wait.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.
Specified by:
`awaitUninterruptibly` in interface `Condition`

