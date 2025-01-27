#### shutdownNow

```
public List<Runnable> shutdownNow()
```
Attempts to stop all actively executing tasks, halts the
processing of waiting tasks, and returns a list of the tasks
that were awaiting execution. These tasks are drained (removed)
from the task queue upon return from this method.This method does not wait for actively executing tasks to
terminate. Use `awaitTermination` to
do that.There are no guarantees beyond best-effort attempts to stop
processing actively executing tasks. This implementation
cancels tasks via `Thread.interrupt()`, so any task that
fails to respond to interrupts may never terminate.
Returns:
list of tasks that never commenced execution
Throws:
`SecurityException` - if a security manager exists and
shutting down this ExecutorService may manipulate
threads that the caller is not permitted to modify
because it does not hold `RuntimePermission``("modifyThread")`,
or the security manager's `checkAccess` method
denies access.

