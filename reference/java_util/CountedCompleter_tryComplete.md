#### tryComplete

```
public final void tryComplete()
```
If the pending count is nonzero, decrements the count;
otherwise invokes `onCompletion(CountedCompleter)`
and then similarly tries to complete this task's completer,
if one exists, else marks this task as complete.

