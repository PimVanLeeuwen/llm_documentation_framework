#### exchange

```
public V exchange(V x,
                  long timeout,
                  TimeUnit unit)
           throws InterruptedException,
                  TimeoutException
```
Waits for another thread to arrive at this exchange point (unless
the current thread is interrupted or
the specified waiting time elapses), and then transfers the given
object to it, receiving its object in return.If another thread is already waiting at the exchange point then
it is resumed for thread scheduling purposes and receives the object
passed in by the current thread. The current thread returns immediately,
receiving the object passed to the exchange by that other thread.If no other thread is already waiting at the exchange then the
current thread is disabled for thread scheduling purposes and lies
dormant until one of three things happens:Some other thread enters the exchange; orSome other thread interrupts
the current thread; orThe specified waiting time elapses.If the current thread:has its interrupted status set on entry to this method; oris interrupted while waiting
for the exchange,then `InterruptedException` is thrown and the current thread's
interrupted status is cleared.If the specified waiting time elapses then `TimeoutException` is thrown. If the time is less than or equal
to zero, the method will not wait at all.
Parameters:
`x` - the object to exchange
`timeout` - the maximum time to wait
`unit` - the time unit of the `timeout` argument
Returns:
the object provided by the other thread
Throws:
`InterruptedException` - if the current thread was
interrupted while waiting
`TimeoutException` - if the specified waiting time elapses
before another thread enters the exchange




