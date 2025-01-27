#### reduce

```
public <U> U reduce(long parallelismThreshold,
                    BiFunction<? super K,? super V,? extends U> transformer,
                    BiFunction<? super U,? super U,? extends U> reducer)
```
Returns the result of accumulating the given transformation
of all (key, value) pairs using the given reducer to
combine values, or null if none.
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
of all (key, value) pairs
Since:
1.8

