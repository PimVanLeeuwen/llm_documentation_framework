#### invokeAny

```
<T> T invokeAny(Collection<? extends Callable<T>> tasks,
                long timeout,
                TimeUnit unit)
         throws InterruptedException,
                ExecutionException,
                TimeoutException
```
Executes the given tasks, returning the result
of one that has completed successfully (i.e., without throwing
an exception), if any do before the given timeout elapses.
Upon normal or exceptional return, tasks that have not
completed are cancelled.
The results of this method are undefined if the given
collection is modified while this operation is in progress.
Type Parameters:
`T` - the type of the values returned from the tasks
Parameters:
`tasks` - the collection of tasks
`timeout` - the maximum time to wait
`unit` - the time unit of the timeout argument
Returns:
the result returned by one of the tasks
Throws:
`InterruptedException` - if interrupted while waiting
`NullPointerException` - if tasks, or unit, or any element
task subject to execution is `null`
`TimeoutException` - if the given timeout elapses before
any task successfully completes
`ExecutionException` - if no task successfully completes
`RejectedExecutionException` - if tasks cannot be scheduled
for execution




