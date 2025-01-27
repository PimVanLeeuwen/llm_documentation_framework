#### getRawResult

```
public T getRawResult()
```
Returns the result of the computation. By default
returns `null`, which is appropriate for `Void`
actions, but in other cases should be overridden, almost
always to return a field or function of a field that
holds the result upon completion.
Specified by:
`getRawResult` in class `ForkJoinTask<T>`
Returns:
the result of the computation

