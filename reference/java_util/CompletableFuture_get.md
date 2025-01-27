#### get

```
public T get(long timeout,
             TimeUnit unit)
      throws InterruptedException,
             ExecutionException,
             TimeoutException
```
Waits if necessary for at most the given time for this future
to complete, and then returns its result, if available.
Specified by:
`get` in interface `Future<T>`
Parameters:
`timeout` - the maximum time to wait
`unit` - the time unit of the timeout argument
Returns:
the result value
Throws:
`CancellationException` - if this future was cancelled
`ExecutionException` - if this future completed exceptionally
`InterruptedException` - if the current thread was interrupted
while waiting
`TimeoutException` - if the wait timed out

