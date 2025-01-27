#### stream

```
public IntStream stream()
```
Returns a stream of indices for which this `BitSet`
contains a bit in the set state. The indices are returned
in order, from lowest to highest. The size of the stream
is the number of bits in the set state, equal to the value
returned by the `cardinality()` method.The bit set must remain constant during the execution of the
terminal stream operation. Otherwise, the result of the terminal
stream operation is undefined.
Returns:
a stream of integers representing set indices
Since:
1.8




