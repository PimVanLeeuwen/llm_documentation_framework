#### get

```
public V get(long timeout,
             TimeUnit unit)
      throws InterruptedException,
             ExecutionException,
             TimeoutException
```
Description copied from interface: `Future`
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
`InterruptedException` - if the current thread was interrupted
while waiting
`ExecutionException` - if the computation threw an
exception
`TimeoutException` - if the wait timed out

