#### setException

```
protected void setException(Throwable t)
```
Causes this future to report an `ExecutionException`
with the given throwable as its cause, unless this future has
already been set or has been cancelled.This method is invoked internally by the `run()` method
upon failure of the computation.
Parameters:
`t` - the cause of failure

