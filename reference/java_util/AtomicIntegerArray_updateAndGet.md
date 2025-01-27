#### updateAndGet

```
public final int updateAndGet(int i,
                              IntUnaryOperator updateFunction)
```
Atomically updates the element at index `i` with the results
of applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.
Parameters:
`i` - the index
`updateFunction` - a side-effect-free function
Returns:
the updated value
Since:
1.8

