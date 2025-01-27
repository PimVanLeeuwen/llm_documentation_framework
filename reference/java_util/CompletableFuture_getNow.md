#### getNow

```
public T getNow(T valueIfAbsent)
```
Returns the result value (or throws any encountered exception)
if completed, else returns the given valueIfAbsent.
Parameters:
`valueIfAbsent` - the value to return if not completed
Returns:
the result value, if completed, else the given valueIfAbsent
Throws:
`CancellationException` - if the computation was cancelled
`CompletionException` - if this future completed
exceptionally or a completion computation threw an exception

