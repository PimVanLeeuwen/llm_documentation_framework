#### reduceKeysToLong

```
public long reduceKeysToLong(long parallelismThreshold,
                             ToLongFunction<? super K> transformer,
                             long basis,
                             LongBinaryOperator reducer)
```
Returns the result of accumulating the given transformation
of all keys using the given reducer to combine values, and
the given basis as an identity value.
Parameters:
`parallelismThreshold` - the (estimated) number of elements
needed for this operation to be executed in parallel
`transformer` - a function returning the transformation
for an element
`basis` - the identity (initial default value) for the reduction
`reducer` - a commutative associative combining function
Returns:
the result of accumulating the given transformation
of all keys
Since:
1.8

