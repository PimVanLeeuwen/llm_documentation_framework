#### onClose

```
S onClose(Runnable closeHandler)
```
Returns an equivalent stream with an additional close handler. Close
handlers are run when the `close()` method
is called on the stream, and are executed in the order they were
added. All close handlers are run, even if earlier close handlers throw
exceptions. If any close handler throws an exception, the first
exception thrown will be relayed to the caller of `close()`, with
any remaining exceptions added to that exception as suppressed exceptions
(unless one of the remaining exceptions is the same exception as the
first exception, since an exception cannot suppress itself.) May
return itself.This is an intermediate
operation.
Parameters:
`closeHandler` - A task to execute when the stream is closed
Returns:
a stream with a handler that is run if the stream is closed

