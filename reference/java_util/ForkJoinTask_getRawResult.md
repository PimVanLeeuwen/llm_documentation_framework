#### getRawResult

```
public abstract V getRawResult()
```
Returns the result that would be returned by `join()`, even
if this task completed abnormally, or `null` if this task
is not known to have been completed. This method is designed
to aid debugging, as well as to support extensions. Its use in
any other context is discouraged.
Returns:
the result, or `null` if not completed

