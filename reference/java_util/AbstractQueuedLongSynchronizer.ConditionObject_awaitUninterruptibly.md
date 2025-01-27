#### awaitUninterruptibly

```
public final void awaitUninterruptibly()
```
Implements uninterruptible condition wait.Save lock state returned by `AbstractQueuedLongSynchronizer.getState()`.Invoke `AbstractQueuedLongSynchronizer.release(long)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled.Reacquire by invoking specialized version of
`AbstractQueuedLongSynchronizer.acquire(long)` with saved state as argument.
Specified by:
`awaitUninterruptibly` in interface `Condition`

