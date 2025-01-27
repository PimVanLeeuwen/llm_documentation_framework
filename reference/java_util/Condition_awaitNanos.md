#### awaitNanos

```
long awaitNanos(long nanosTimeout)
         throws InterruptedException
```
Causes the current thread to wait until it is signalled or interrupted,
or the specified waiting time elapses.The lock associated with this condition is atomically
released and the current thread becomes disabled for thread scheduling
purposes and lies dormant until one of five things happens:Some other thread invokes the `signal()` method for this
`Condition` and the current thread happens to be chosen as the
thread to be awakened; orSome other thread invokes the `signalAll()` method for this
`Condition`; orSome other thread interrupts the
current thread, and interruption of thread suspension is supported; orThe specified waiting time elapses; orA "spurious wakeup" occurs.In all cases, before this method can return the current thread must
re-acquire the lock associated with this condition. When the
thread returns it is guaranteed to hold this lock.If the current thread:has its interrupted status set on entry to this method; oris interrupted while waiting
and interruption of thread suspension is supported,then `InterruptedException` is thrown and the current thread's
interrupted status is cleared. It is not specified, in the first
case, whether or not the test for interruption occurs before the lock
is released.The method returns an estimate of the number of nanoseconds
remaining to wait given the supplied `nanosTimeout`
value upon return, or a value less than or equal to zero if it
timed out. This value can be used to determine whether and how
long to re-wait in cases where the wait returns but an awaited
condition still does not hold. Typical uses of this method take
the following form:
```
 
 boolean aMethod(long timeout, TimeUnit unit) {
   long nanos = unit.toNanos(timeout);
   lock.lock();
   try {
     while (!conditionBeingWaitedFor()) {
       if (nanos <= 0L)
         return false;
       nanos = theCondition.awaitNanos(nanos);
     }
     // ...
   } finally {
     lock.unlock();
   }
 }
```
Design note: This method requires a nanosecond argument so
as to avoid truncation errors in reporting remaining times.
Such precision loss would make it difficult for programmers to
ensure that total waiting times are not systematically shorter
than specified when re-waits occur.Implementation ConsiderationsThe current thread is assumed to hold the lock associated with this
`Condition` when this method is called.
It is up to the implementation to determine if this is
the case and if not, how to respond. Typically, an exception will be
thrown (such as `IllegalMonitorStateException`) and the
implementation must document that fact.An implementation can favor responding to an interrupt over normal
method return in response to a signal, or over indicating the elapse
of the specified waiting time. In either case the implementation
must ensure that the signal is redirected to another waiting thread, if
there is one.
Parameters:
`nanosTimeout` - the maximum time to wait, in nanoseconds
Returns:
an estimate of the `nanosTimeout` value minus
the time spent waiting upon return from this method.
A positive value may be used as the argument to a
subsequent call to this method to finish waiting out
the desired time. A value less than or equal to zero
indicates that no time remains.
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

