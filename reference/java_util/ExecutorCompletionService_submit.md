#### submit

```
public Future<V> submit(Runnable task,
                        V result)
```
Description copied from interface: `CompletionService`
Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.
Specified by:
`submit` in interface `CompletionService<V>`
Parameters:
`task` - the task to submit
`result` - the result to return upon successful completion
Returns:
a Future representing pending completion of the task,
and whose `get()` method will return the given
result value upon completion

