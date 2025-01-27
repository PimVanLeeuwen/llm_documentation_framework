#### tryAcquire

```
public boolean tryAcquire(int permits,
                          long timeout,
                          TimeUnit unit)
                   throws InterruptedException
```
Acquires the given number of permits from this semaphore, if all
become available within the given waiting time and the current
thread has not been interrupted.Acquires the given number of permits, if they are available and
returns immediately, with the value `true`,
reducing the number of available permits by the given amount.If insufficient permits are available then
the current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:Some other thread invokes one of the `release`
methods for this semaphore, the current thread is next to be assigned
permits and the number of available permits satisfies this request; orSome other thread interrupts
the current thread; orThe specified waiting time elapses.If the permits are acquired then the value `true` is returned.If the current thread:has its interrupted status set on entry to this method; oris interrupted while waiting
to acquire the permits,then `InterruptedException` is thrown and the current thread's
interrupted status is cleared.
Any permits that were to be assigned to this thread, are instead
assigned to other threads trying to acquire permits, as if
the permits had been made available by a call to `release()`.If the specified waiting time elapses then the value `false`
is returned. If the time is less than or equal to zero, the method
will not wait at all. Any permits that were to be assigned to this
thread, are instead assigned to other threads trying to acquire
permits, as if the permits had been made available by a call to
`release()`.
Parameters:
`permits` - the number of permits to acquire
`timeout` - the maximum time to wait for the permits
`unit` - the time unit of the `timeout` argument
Returns:
`true` if all permits were acquired and `false`
if the waiting time elapsed before all permits were acquired
Throws:
`InterruptedException` - if the current thread is interrupted
`IllegalArgumentException` - if `permits` is negative

