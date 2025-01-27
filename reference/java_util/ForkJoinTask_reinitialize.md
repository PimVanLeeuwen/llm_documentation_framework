#### reinitialize

```
public void reinitialize()
```
Resets the internal bookkeeping state of this task, allowing a
subsequent `fork`. This method allows repeated reuse of
this task, but only if reuse occurs when this task has either
never been forked, or has been forked, then completed and all
outstanding joins of this task have also completed. Effects
under any other usage conditions are not guaranteed.
This method may be useful when executing
pre-constructed trees of subtasks in loops.Upon completion of this method, `isDone()` reports
`false`, and `getException()` reports `null`. However, the value returned by `getRawResult` is
unaffected. To clear this value, you can invoke `setRawResult(null)`.

