#### hasQueuedThread

```
public final boolean hasQueuedThread(Thread thread)
```
Queries whether the given thread is waiting to acquire this
lock. Note that because cancellations may occur at any time, a
`true` return does not guarantee that this thread
will ever acquire this lock. This method is designed primarily for use
in monitoring of the system state.
Parameters:
`thread` - the thread
Returns:
`true` if the given thread is queued waiting for this lock
Throws:
`NullPointerException` - if the thread is null

