#### forEachKey

```
public <U> void forEachKey(long parallelismThreshold,
                           Function<? super K,? extends U> transformer,
                           Consumer<? super U> action)
```
Performs the given action for each non-null transformation
of each key.
Type Parameters:
`U` - the return type of the transformer
Parameters:
`parallelismThreshold` - the (estimated) number of elements
needed for this operation to be executed in parallel
`transformer` - a function returning the transformation
for an element, or null if there is no transformation (in
which case the action is not applied)
`action` - the action
Since:
1.8

