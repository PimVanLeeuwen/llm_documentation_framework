#### firstComplete

```
public final CountedCompleter<?> firstComplete()
```
If this task's pending count is zero, returns this task;
otherwise decrements its pending count and returns `null`. This method is designed to be used with `nextComplete()` in completion traversal loops.
Returns:
this task, if pending count was zero, else `null`

