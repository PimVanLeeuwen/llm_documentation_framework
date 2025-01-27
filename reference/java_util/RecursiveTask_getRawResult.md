#### getRawResult

```
public final V getRawResult()
```
Description copied from class: `ForkJoinTask`
Returns the result that would be returned by `ForkJoinTask.join()`, even
if this task completed abnormally, or `null` if this task
is not known to have been completed. This method is designed
to aid debugging, as well as to support extensions. Its use in
any other context is discouraged.
Specified by:
`getRawResult` in class `ForkJoinTask<V>`
Returns:
the result, or `null` if not completed

