#### scheduleAtFixedRate

```
public ScheduledFuture<?> scheduleAtFixedRate(Runnable command,
                                              long initialDelay,
                                              long period,
                                              TimeUnit unit)
```
Description copied from interface: `ScheduledExecutorService`
Creates and executes a periodic action that becomes enabled first
after the given initial delay, and subsequently with the given
period; that is executions will commence after
`initialDelay` then `initialDelay+period`, then
`initialDelay + 2 * period`, and so on.
If any execution of the task
encounters an exception, subsequent executions are suppressed.
Otherwise, the task will only terminate via cancellation or
termination of the executor. If any execution of this task
takes longer than its period, then subsequent executions
may start late, but will not concurrently execute.
Specified by:
`scheduleAtFixedRate` in interface `ScheduledExecutorService`
Parameters:
`command` - the task to execute
`initialDelay` - the time to delay first execution
`period` - the period between successive executions
`unit` - the time unit of the initialDelay and period parameters
Returns:
a ScheduledFuture representing pending completion of
the task, and whose `get()` method will throw an
exception upon cancellation
Throws:
`RejectedExecutionException` - if the task cannot be
scheduled for execution
`NullPointerException` - if command is null
`IllegalArgumentException` - if period less than or equal to zero

