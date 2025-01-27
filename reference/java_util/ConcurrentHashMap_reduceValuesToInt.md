#### reduceValuesToInt

```
public int reduceValuesToInt(long parallelismThreshold,
                             ToIntFunction<? super V> transformer,
                             int basis,
                             IntBinaryOperator reducer)
```
Returns the result of accumulating the given transformation
of all values using the given reducer to combine values,
and the given basis as an identity value.
Parameters:
`parallelismThreshold` - the (estimated) number of elements
needed for this operation to be executed in parallel
`transformer` - a function returning the transformation
for an element
`basis` - the identity (initial default value) for the reduction
`reducer` - a commutative associative combining function
Returns:
the result of accumulating the given transformation
of all values
Since:
1.8

