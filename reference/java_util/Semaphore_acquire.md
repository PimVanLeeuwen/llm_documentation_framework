#### acquire

```
public void acquire(int permits)
             throws InterruptedException
```
Acquires the given number of permits from this semaphore,
blocking until all are available,
or the thread is interrupted.Acquires the given number of permits, if they are available,
and returns immediately, reducing the number of available permits
by the given amount.If insufficient permits are available then the current thread becomes
disabled for thread scheduling purposes and lies dormant until
one of two things happens:Some other thread invokes one of the `release`
methods for this semaphore, the current thread is next to be assigned
permits and the number of available permits satisfies this request; orSome other thread interrupts
the current thread.If the current thread:has its interrupted status set on entry to this method; oris interrupted while waiting
for a permit,then `InterruptedException` is thrown and the current thread's
interrupted status is cleared.
Any permits that were to be assigned to this thread are instead
assigned to other threads trying to acquire permits, as if
permits had been made available by a call to `release()`.
Parameters:
`permits` - the number of permits to acquire
Throws:
`InterruptedException` - if the current thread is interrupted
`IllegalArgumentException` - if `permits` is negative

