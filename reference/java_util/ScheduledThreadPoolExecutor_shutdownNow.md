#### shutdownNow

```
public List<Runnable> shutdownNow()
```
Attempts to stop all actively executing tasks, halts the
processing of waiting tasks, and returns a list of the tasks
that were awaiting execution.This method does not wait for actively executing tasks to
terminate. Use `awaitTermination` to
do that.There are no guarantees beyond best-effort attempts to stop
processing actively executing tasks. This implementation
cancels tasks via `Thread.interrupt()`, so any task that
fails to respond to interrupts may never terminate.
Specified by:
`shutdownNow` in interface `ExecutorService`
Overrides:
`shutdownNow` in class `ThreadPoolExecutor`
Returns:
list of tasks that never commenced execution.
Each element of this list is a `ScheduledFuture`,
including those tasks submitted using `execute`,
which are for scheduling purposes used as the basis of a
zero-delay `ScheduledFuture`.
Throws:
`SecurityException` - if a security manager exists and
shutting down this ExecutorService may manipulate
threads that the caller is not permitted to modify
because it does not hold `RuntimePermission``("modifyThread")`,
or the security manager's `checkAccess` method
denies access.

