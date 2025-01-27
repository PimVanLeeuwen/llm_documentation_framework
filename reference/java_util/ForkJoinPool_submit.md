#### submit

```
public ForkJoinTask<?> submit(Runnable task)
```
Description copied from interface: `ExecutorService`
Submits a Runnable task for execution and returns a Future
representing that task. The Future's `get` method will
return `null` upon successful completion.
Specified by:
`submit` in interface `ExecutorService`
Overrides:
`submit` in class `AbstractExecutorService`
Parameters:
`task` - the task to submit
Returns:
a Future representing pending completion of the task
Throws:
`NullPointerException` - if the task is null
`RejectedExecutionException` - if the task cannot be
scheduled for execution

