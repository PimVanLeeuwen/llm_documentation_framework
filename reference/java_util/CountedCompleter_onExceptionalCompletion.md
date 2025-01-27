#### onExceptionalCompletion

```
public boolean onExceptionalCompletion(Throwable ex,
                                       CountedCompleter<?> caller)
```
Performs an action when method `ForkJoinTask.completeExceptionally(Throwable)` is invoked or method `compute()` throws an exception, and this task has not already
otherwise completed normally. On entry to this method, this task
`ForkJoinTask.isCompletedAbnormally()`. The return value
of this method controls further propagation: If `true`
and this task has a completer that has not completed, then that
completer is also completed exceptionally, with the same
exception as this completer. The default implementation of
this method does nothing except return `true`.
Parameters:
`ex` - the exception
`caller` - the task invoking this method (which may
be this task itself)
Returns:
`true` if this exception should be propagated to this
task's completer, if one exists

