#### submit

```
Future<V> submit(Runnable task,
                 V result)
```
Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.
Parameters:
`task` - the task to submit
`result` - the result to return upon successful completion
Returns:
a Future representing pending completion of the task,
and whose `get()` method will return the given
result value upon completion
Throws:
`RejectedExecutionException` - if the task cannot be
scheduled for execution
`NullPointerException` - if the task is null

