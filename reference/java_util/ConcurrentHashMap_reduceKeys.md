#### reduceKeys

```
public <U> U reduceKeys(long parallelismThreshold,
                        Function<? super K,? extends U> transformer,
                        BiFunction<? super U,? super U,? extends U> reducer)
```
Returns the result of accumulating the given transformation
of all keys using the given reducer to combine values, or
null if none.
Type Parameters:
`U` - the return type of the transformer
Parameters:
`parallelismThreshold` - the (estimated) number of elements
needed for this operation to be executed in parallel
`transformer` - a function returning the transformation
for an element, or null if there is no transformation (in
which case it is not combined)
`reducer` - a commutative associative combining function
Returns:
the result of accumulating the given transformation
of all keys
Since:
1.8

