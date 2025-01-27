#### callable

```
public static Callable<Object> callable(PrivilegedExceptionAction<?> action)
```
Returns a `Callable` object that, when
called, runs the given privileged exception action and returns
its result.
Parameters:
`action` - the privileged exception action to run
Returns:
a callable object
Throws:
`NullPointerException` - if action null

