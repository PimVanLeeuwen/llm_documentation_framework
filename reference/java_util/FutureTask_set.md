#### set

```
protected void set(V v)
```
Sets the result of this future to the given value unless
this future has already been set or has been cancelled.This method is invoked internally by the `run()` method
upon successful completion of the computation.
Parameters:
`v` - the value

