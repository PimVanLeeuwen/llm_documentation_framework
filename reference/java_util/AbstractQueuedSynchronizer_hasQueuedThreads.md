#### hasQueuedThreads

```
public final boolean hasQueuedThreads()
```
Queries whether any threads are waiting to acquire. Note that
because cancellations due to interrupts and timeouts may occur
at any time, a `true` return does not guarantee that any
other thread will ever acquire.In this implementation, this operation returns in
constant time.
Returns:
`true` if there may be other threads waiting to acquire

