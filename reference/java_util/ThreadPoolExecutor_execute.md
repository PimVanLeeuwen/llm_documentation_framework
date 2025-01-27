#### execute

```
public void execute(Runnable command)
```
Executes the given task sometime in the future. The task
may execute in a new thread or in an existing pooled thread.
If the task cannot be submitted for execution, either because this
executor has been shutdown or because its capacity has been reached,
the task is handled by the current `RejectedExecutionHandler`.
Parameters:
`command` - the task to execute
Throws:
`RejectedExecutionException` - at discretion of
`RejectedExecutionHandler`, if the task
cannot be accepted for execution
`NullPointerException` - if `command` is null

