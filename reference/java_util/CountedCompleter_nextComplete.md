#### nextComplete

```
public final CountedCompleter<?> nextComplete()
```
If this task does not have a completer, invokes `ForkJoinTask.quietlyComplete()` and returns `null`. Or, if
the completer's pending count is non-zero, decrements that
pending count and returns `null`. Otherwise, returns the
completer. This method can be used as part of a completion
traversal loop for homogeneous task hierarchies:
```
 
 for (CountedCompleter<?> c = firstComplete();
      c != null;
      c = c.nextComplete()) {
   // ... process c ...
 }
```

Returns:
the completer, or `null` if none

