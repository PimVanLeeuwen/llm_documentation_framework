#### await

```
public int await(long timeout,
                 TimeUnit unit)
          throws InterruptedException,
                 BrokenBarrierException,
                 TimeoutException
```
Waits until all parties have invoked
`await` on this barrier, or the specified waiting time elapses.If the current thread is not the last to arrive then it is
disabled for thread scheduling purposes and lies dormant until
one of the following things happens:The last thread arrives; orThe specified timeout elapses; orSome other thread interrupts
the current thread; orSome other thread interrupts
one of the other waiting threads; orSome other thread times out while waiting for barrier; orSome other thread invokes `reset()` on this barrier.If the current thread:has its interrupted status set on entry to this method; oris interrupted while waitingthen `InterruptedException` is thrown and the current thread's
interrupted status is cleared.If the specified waiting time elapses then `TimeoutException`
is thrown. If the time is less than or equal to zero, the
method will not wait at all.If the barrier is `reset()` while any thread is waiting,
or if the barrier is broken when
`await` is invoked, or while any thread is waiting, then
`BrokenBarrierException` is thrown.If any thread is interrupted while
waiting, then all other waiting threads will throw `BrokenBarrierException` and the barrier is placed in the broken
state.If the current thread is the last thread to arrive, and a
non-null barrier action was supplied in the constructor, then the
current thread runs the action before allowing the other threads to
continue.
If an exception occurs during the barrier action then that exception
will be propagated in the current thread and the barrier is placed in
the broken state.
Parameters:
`timeout` - the time to wait for the barrier
`unit` - the time unit of the timeout parameter
Returns:
the arrival index of the current thread, where index
`getParties() - 1` indicates the first
to arrive and zero indicates the last to arrive
Throws:
`InterruptedException` - if the current thread was interrupted
while waiting
`TimeoutException` - if the specified timeout elapses.
In this case the barrier will be broken.
`BrokenBarrierException` - if another thread was
interrupted or timed out while the current thread was
waiting, or the barrier was reset, or the barrier was broken
when `await` was called, or the barrier action (if
present) failed due to an exception

