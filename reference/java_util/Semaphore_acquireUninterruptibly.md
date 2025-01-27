#### acquireUninterruptibly

```
public void acquireUninterruptibly(int permits)
```
Acquires the given number of permits from this semaphore,
blocking until all are available.Acquires the given number of permits, if they are available,
and returns immediately, reducing the number of available permits
by the given amount.If insufficient permits are available then the current thread becomes
disabled for thread scheduling purposes and lies dormant until
some other thread invokes one of the `release`
methods for this semaphore, the current thread is next to be assigned
permits and the number of available permits satisfies this request.If the current thread is interrupted
while waiting for permits then it will continue to wait and its
position in the queue is not affected. When the thread does return
from this method its interrupt status will be set.
Parameters:
`permits` - the number of permits to acquire
Throws:
`IllegalArgumentException` - if `permits` is negative

