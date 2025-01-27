#### execute

```
void execute(Runnable command)
```
Executes the given command at some time in the future. The command
may execute in a new thread, in a pooled thread, or in the calling
thread, at the discretion of the `Executor` implementation.
Parameters:
`command` - the runnable task
Throws:
`RejectedExecutionException` - if this task cannot be
accepted for execution
`NullPointerException` - if command is null




