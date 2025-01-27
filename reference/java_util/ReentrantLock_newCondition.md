#### newCondition

```
public Condition newCondition()
```
Returns a `Condition` instance for use with this
`Lock` instance.The returned `Condition` instance supports the same
usages as do the `Object` monitor methods (`wait`, `notify`, and `notifyAll`) when used with the built-in
monitor lock.If this lock is not held when any of the `Condition`
waiting or signalling methods are called, then an `IllegalMonitorStateException` is thrown.When the condition waiting
methods are called the lock is released and, before they
return, the lock is reacquired and the lock hold count restored
to what it was when the method was called.If a thread is interrupted
while waiting then the wait will terminate, an `InterruptedException` will be thrown, and the thread's
interrupted status will be cleared.Waiting threads are signalled in FIFO order.The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for fair locks favors those threads that have been
waiting the longest.
Specified by:
`newCondition` in interface `Lock`
Returns:
the Condition object

