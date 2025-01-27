#### unconfigurableScheduledExecutorService

```
public static ScheduledExecutorService unconfigurableScheduledExecutorService(ScheduledExecutorService executor)
```
Returns an object that delegates all defined `ScheduledExecutorService` methods to the given executor, but
not any other methods that might otherwise be accessible using
casts. This provides a way to safely "freeze" configuration and
disallow tuning of a given concrete implementation.
Parameters:
`executor` - the underlying implementation
Returns:
a `ScheduledExecutorService` instance
Throws:
`NullPointerException` - if executor null

