#### privilegedCallableUsingCurrentClassLoader

```
public static <T> Callable<T> privilegedCallableUsingCurrentClassLoader(Callable<T> callable)
```
Returns a `Callable` object that will, when called,
execute the given `callable` under the current access
control context, with the current context class loader as the
context class loader. This method should normally be invoked
within an
`AccessController.doPrivileged`
action to create callables that will, if possible, execute
under the selected permission settings holding within that
action; or if not possible, throw an associated `AccessControlException`.
Type Parameters:
`T` - the type of the callable's result
Parameters:
`callable` - the underlying task
Returns:
a callable object
Throws:
`NullPointerException` - if callable null
`AccessControlException` - if the current access control
context does not have permission to both set and get context
class loader




