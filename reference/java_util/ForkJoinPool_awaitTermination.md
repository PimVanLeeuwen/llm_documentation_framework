#### awaitTermination

```
public boolean awaitTermination(long timeout,
                                TimeUnit unit)
                         throws InterruptedException
```
Blocks until all tasks have completed execution after a
shutdown request, or the timeout occurs, or the current thread
is interrupted, whichever happens first. Because the `commonPool()` never terminates until program shutdown, when
applied to the common pool, this method is equivalent to `awaitQuiescence(long, TimeUnit)` but always returns `false`.
Parameters:
`timeout` - the maximum time to wait
`unit` - the time unit of the timeout argument
Returns:
`true` if this executor terminated and
`false` if the timeout elapsed before termination
Throws:
`InterruptedException` - if interrupted while waiting

