#### submit

```
Future<?> submit(Runnable task)
```
Submits a Runnable task for execution and returns a Future
representing that task. The Future's `get` method will
return `null` upon successful completion.
Parameters:
`task` - the task to submit
Returns:
a Future representing pending completion of the task
Throws:
`RejectedExecutionException` - if the task cannot be
scheduled for execution
`NullPointerException` - if the task is null

