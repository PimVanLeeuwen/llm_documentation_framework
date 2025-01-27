#### execute

```
public void execute(Runnable command)
```
Executes `command` with zero required delay.
This has effect equivalent to
`schedule(command, 0, anyUnit)`.
Note that inspections of the queue and of the list returned by
`shutdownNow` will access the zero-delayed
`ScheduledFuture`, not the `command` itself.A consequence of the use of `ScheduledFuture` objects is
that `afterExecute` is always
called with a null second `Throwable` argument, even if the
`command` terminated abruptly. Instead, the `Throwable`
thrown by such a task can be obtained via `Future.get()`.
Specified by:
`execute` in interface `Executor`
Overrides:
`execute` in class `ThreadPoolExecutor`
Parameters:
`command` - the task to execute
Throws:
`RejectedExecutionException` - at discretion of
`RejectedExecutionHandler`, if the task
cannot be accepted for execution because the
executor has been shut down
`NullPointerException` - if `command` is null

