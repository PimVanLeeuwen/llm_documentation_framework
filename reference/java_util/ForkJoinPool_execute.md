#### execute

```
public void execute(Runnable task)
```
Description copied from interface: `Executor`
Executes the given command at some time in the future. The command
may execute in a new thread, in a pooled thread, or in the calling
thread, at the discretion of the `Executor` implementation.
Parameters:
`task` - the runnable task
Throws:
`NullPointerException` - if the task is null
`RejectedExecutionException` - if the task cannot be
scheduled for execution

