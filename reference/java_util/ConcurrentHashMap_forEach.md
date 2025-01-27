#### forEach

```
public <U> void forEach(long parallelismThreshold,
                        BiFunction<? super K,? super V,? extends U> transformer,
                        Consumer<? super U> action)
```
Performs the given action for each non-null transformation
of each (key, value).
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

