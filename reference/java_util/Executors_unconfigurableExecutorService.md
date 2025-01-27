#### unconfigurableExecutorService

```
public static ExecutorService unconfigurableExecutorService(ExecutorService executor)
```
Returns an object that delegates all defined `ExecutorService` methods to the given executor, but not any
other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.
Parameters:
`executor` - the underlying implementation
Returns:
an `ExecutorService` instance
Throws:
`NullPointerException` - if executor null

