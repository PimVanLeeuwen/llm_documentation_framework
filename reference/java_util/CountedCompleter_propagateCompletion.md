#### propagateCompletion

```
public final void propagateCompletion()
```
Equivalent to `tryComplete()` but does not invoke `onCompletion(CountedCompleter)` along the completion path:
If the pending count is nonzero, decrements the count;
otherwise, similarly tries to complete this task's completer, if
one exists, else marks this task as complete. This method may be
useful in cases where `onCompletion` should not, or need
not, be invoked for each completer in a computation.

