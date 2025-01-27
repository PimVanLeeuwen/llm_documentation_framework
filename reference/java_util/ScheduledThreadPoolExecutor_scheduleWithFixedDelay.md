#### scheduleWithFixedDelay

```
public ScheduledFuture<?> scheduleWithFixedDelay(Runnable command,
                                                 long initialDelay,
                                                 long delay,
                                                 TimeUnit unit)
```
Description copied from interface: `ScheduledExecutorService`
Creates and executes a periodic action that becomes enabled first
after the given initial delay, and subsequently with the
given delay between the termination of one execution and the
commencement of the next. If any execution of the task
encounters an exception, subsequent executions are suppressed.
Otherwise, the task will only terminate via cancellation or
termination of the executor.
Specified by:
`scheduleWithFixedDelay` in interface `ScheduledExecutorService`
Parameters:
`command` - the task to execute
`initialDelay` - the time to delay first execution
`delay` - the delay between the termination of one
execution and the commencement of the next
`unit` - the time unit of the initialDelay and delay parameters
Returns:
a ScheduledFuture representing pending completion of
the task, and whose `get()` method will throw an
exception upon cancellation
Throws:
`RejectedExecutionException` - if the task cannot be
scheduled for execution
`NullPointerException` - if command is null
`IllegalArgumentException` - if delay less than or equal to zero

