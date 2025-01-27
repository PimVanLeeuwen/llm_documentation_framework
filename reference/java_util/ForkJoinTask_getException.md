#### getException

```
public final Throwable getException()
```
Returns the exception thrown by the base computation, or a
`CancellationException` if cancelled, or `null` if
none or if the method has not yet completed.
Returns:
the exception, or `null` if none

