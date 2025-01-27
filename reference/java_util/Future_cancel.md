#### cancel

```
boolean cancel(boolean mayInterruptIfRunning)
```
Attempts to cancel execution of this task. This attempt will
fail if the task has already completed, has already been cancelled,
or could not be cancelled for some other reason. If successful,
and this task has not started when `cancel` is called,
this task should never run. If the task has already started,
then the `mayInterruptIfRunning` parameter determines
whether the thread executing this task should be interrupted in
an attempt to stop the task.After this method returns, subsequent calls to `isDone()` will
always return `true`. Subsequent calls to `isCancelled()`
will always return `true` if this method returned `true`.
Parameters:
`mayInterruptIfRunning` - `true` if the thread executing this
task should be interrupted; otherwise, in-progress tasks are allowed
to complete
Returns:
`false` if the task could not be cancelled,
typically because it has already completed normally;
`true` otherwise

