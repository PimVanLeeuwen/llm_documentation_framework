#### search

```
public <U> U search(long parallelismThreshold,
                    BiFunction<? super K,? super V,? extends U> searchFunction)
```
Returns a non-null result from applying the given search
function on each (key, value), or null if none. Upon
success, further element processing is suppressed and the
results of any other parallel invocations of the search
function are ignored.
Type Parameters:
`U` - the return type of the search function
Parameters:
`parallelismThreshold` - the (estimated) number of elements
needed for this operation to be executed in parallel
`searchFunction` - a function returning a non-null
result on success, else null
Returns:
a non-null result from applying the given search
function on each (key, value), or null if none
Since:
1.8

