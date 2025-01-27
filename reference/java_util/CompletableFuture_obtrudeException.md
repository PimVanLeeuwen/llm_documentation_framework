#### obtrudeException

```
public void obtrudeException(Throwable ex)
```
Forcibly causes subsequent invocations of method `get()`
and related methods to throw the given exception, whether or
not already completed. This method is designed for use only in
error recovery actions, and even in such situations may result
in ongoing dependent completions using established versus
overwritten outcomes.
Parameters:
`ex` - the exception
Throws:
`NullPointerException` - if the exception is null

