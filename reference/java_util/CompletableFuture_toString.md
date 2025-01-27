#### toString

```
public String toString()
```
Returns a string identifying this CompletableFuture, as well as
its completion state. The state, in brackets, contains the
String `"Completed Normally"` or the String `"Completed Exceptionally"`, or the String `"Not
completed"` followed by the number of CompletableFutures
dependent upon its completion, if any.
Overrides:
`toString` in class `Object`
Returns:
a string identifying this CompletableFuture, as well as its state




