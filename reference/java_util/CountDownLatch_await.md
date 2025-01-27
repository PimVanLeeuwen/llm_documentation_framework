#### await

```
public boolean await(long timeout,
                     TimeUnit unit)
              throws InterruptedException
```
Causes the current thread to wait until the latch has counted down to
zero, unless the thread is interrupted,
or the specified waiting time elapses.If the current count is zero then this method returns immediately
with the value `true`.If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:The count reaches zero due to invocations of the
`countDown()` method; orSome other thread interrupts
the current thread; orThe specified waiting time elapses.If the count reaches zero then the method returns with the
value `true`.If the current thread:has its interrupted status set on entry to this method; oris interrupted while waiting,then `InterruptedException` is thrown and the current thread's
interrupted status is cleared.If the specified waiting time elapses then the value `false`
is returned. If the time is less than or equal to zero, the method
will not wait at all.
Parameters:
`timeout` - the maximum time to wait
`unit` - the time unit of the `timeout` argument
Returns:
`true` if the count reached zero and `false`
if the waiting time elapsed before the count reached zero
Throws:
`InterruptedException` - if the current thread is interrupted
while waiting

