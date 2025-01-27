#### schedule

```
public <V> ScheduledFuture<V> schedule(Callable<V> callable,
                                       long delay,
                                       TimeUnit unit)
```
Description copied from interface: `ScheduledExecutorService`
Creates and executes a ScheduledFuture that becomes enabled after the
given delay.
Specified by:
`schedule` in interface `ScheduledExecutorService`
Type Parameters:
`V` - the type of the callable's result
Parameters:
`callable` - the function to execute
`delay` - the time from now to delay execution
`unit` - the time unit of the delay parameter
Returns:
a ScheduledFuture that can be used to extract result or cancel
Throws:
`RejectedExecutionException` - if the task cannot be
scheduled for execution
`NullPointerException` - if callable is null

