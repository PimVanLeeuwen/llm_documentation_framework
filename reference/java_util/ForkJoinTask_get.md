#### get

```
public final V get(long timeout,
                   TimeUnit unit)
            throws InterruptedException,
                   ExecutionException,
                   TimeoutException
```
Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.
Specified by:
`get` in interface `Future<V>`
Parameters:
`timeout` - the maximum time to wait
`unit` - the time unit of the timeout argument
Returns:
the computed result
Throws:
`CancellationException` - if the computation was cancelled
`ExecutionException` - if the computation threw an
exception
`InterruptedException` - if the current thread is not a
member of a ForkJoinPool and was interrupted while waiting
`TimeoutException` - if the wait timed out

