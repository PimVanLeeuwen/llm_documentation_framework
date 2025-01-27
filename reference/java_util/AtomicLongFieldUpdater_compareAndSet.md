#### compareAndSet

```
public abstract boolean compareAndSet(T obj,
                                      long expect,
                                      long update)
```
Atomically sets the field of the given object managed by this updater
to the given updated value if the current value `==` the
expected value. This method is guaranteed to be atomic with respect to
other calls to `compareAndSet` and `set`, but not
necessarily with respect to other changes in the field.
Parameters:
`obj` - An object whose field to conditionally set
`expect` - the expected value
`update` - the new value
Returns:
`true` if successful
Throws:
`ClassCastException` - if `obj` is not an instance
of the class possessing the field established in the constructor

