#### setRawResult

```
protected void setRawResult(T t)
```
A method that result-bearing CountedCompleters may optionally
use to help maintain result data. By default, does nothing.
Overrides are not recommended. However, if this method is
overridden to update existing objects or fields, then it must
in general be defined to be thread-safe.
Specified by:
`setRawResult` in class `ForkJoinTask<T>`
Parameters:
`t` - the value




