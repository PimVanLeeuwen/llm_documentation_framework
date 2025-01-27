#### set

```
public abstract void set(T obj,
                         V newValue)
```
Sets the field of the given object managed by this updater to the
given updated value. This operation is guaranteed to act as a volatile
store with respect to subsequent invocations of `compareAndSet`.
Parameters:
`obj` - An object whose field to set
`newValue` - the new value

