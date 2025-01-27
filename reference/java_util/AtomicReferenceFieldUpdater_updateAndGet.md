#### updateAndGet

```
public final V updateAndGet(T obj,
                            UnaryOperator<V> updateFunction)
```
Atomically updates the field of the given object managed by this updater
with the results of applying the given function, returning the updated
value. The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among threads.
Parameters:
`obj` - An object whose field to get and set
`updateFunction` - a side-effect-free function
Returns:
the updated value
Since:
1.8

