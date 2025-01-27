#### shutdown

```
public void shutdown()
```
Initiates an orderly shutdown in which previously submitted
tasks are executed, but no new tasks will be accepted.
Invocation has no additional effect if already shut down.This method does not wait for previously submitted tasks to
complete execution. Use `awaitTermination`
to do that.If the `ExecuteExistingDelayedTasksAfterShutdownPolicy`
has been set `false`, existing delayed tasks whose delays
have not yet elapsed are cancelled. And unless the `ContinueExistingPeriodicTasksAfterShutdownPolicy` has been set
`true`, future executions of existing periodic tasks will
be cancelled.
Specified by:
`shutdown` in interface `ExecutorService`
Overrides:
`shutdown` in class `ThreadPoolExecutor`
Throws:
`SecurityException` - if a security manager exists and
shutting down this ExecutorService may manipulate
threads that the caller is not permitted to modify
because it does not hold `RuntimePermission``("modifyThread")`,
or the security manager's `checkAccess` method
denies access.

