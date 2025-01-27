#### signal

```
void signal()
```
Wakes up one waiting thread.If any threads are waiting on this condition then one
is selected for waking up. That thread must then re-acquire the
lock before returning from `await`.Implementation ConsiderationsAn implementation may (and typically does) require that the
current thread hold the lock associated with this `Condition` when this method is called. Implementations must
document this precondition and any actions taken if the lock is
not held. Typically, an exception such as `IllegalMonitorStateException` will be thrown.

