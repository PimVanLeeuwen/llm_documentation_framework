```
public class TimeoutException
extends Exception
```
Exception thrown when a blocking operation times out. Blocking
operations for which a timeout is specified need a means to
indicate that the timeout has occurred. For many such operations it
is possible to return a value that indicates timeout; when that is
not possible or desirable then `TimeoutException` should be
declared and thrown.
Since:
1.5
See Also:
Serialized Form
