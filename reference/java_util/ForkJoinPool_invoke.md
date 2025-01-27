#### invoke

```
public <T> T invoke(ForkJoinTask<T> task)
```
Performs the given task, returning its result upon completion.
If the computation encounters an unchecked Exception or Error,
it is rethrown as the outcome of this invocation. Rethrown
exceptions behave in the same way as regular exceptions, but,
when possible, contain stack traces (as displayed for example
using `ex.printStackTrace()`) of both the current thread
as well as the thread actually encountering the exception;
minimally only the latter.
Type Parameters:
`T` - the type of the task's result
Parameters:
`task` - the task
Returns:
the task's result
Throws:
`NullPointerException` - if the task is null
`RejectedExecutionException` - if the task cannot be
scheduled for execution

