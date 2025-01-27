#### awaitTermination

```
public boolean awaitTermination(long timeout,
                                TimeUnit unit)
                         throws InterruptedException
```
Description copied from interface: `ExecutorService`
Blocks until all tasks have completed execution after a shutdown
request, or the timeout occurs, or the current thread is
interrupted, whichever happens first.
Parameters:
`timeout` - the maximum time to wait
`unit` - the time unit of the timeout argument
Returns:
`true` if this executor terminated and
`false` if the timeout elapsed before termination
Throws:
`InterruptedException` - if interrupted while waiting

