#### getNumberOfDependents

```
public int getNumberOfDependents()
```
Returns the estimated number of CompletableFutures whose
completions are awaiting completion of this CompletableFuture.
This method is designed for use in monitoring system state, not
for synchronization control.
Returns:
the number of dependent CompletableFutures

