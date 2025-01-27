#### getQueuedTaskCount

```
public static int getQueuedTaskCount()
```
Returns an estimate of the number of tasks that have been
forked by the current worker thread but not yet executed. This
value may be useful for heuristic decisions about whether to
fork other tasks.
Returns:
the number of tasks

