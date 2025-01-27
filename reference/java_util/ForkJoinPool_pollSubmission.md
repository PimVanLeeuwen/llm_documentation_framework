#### pollSubmission

```
protected ForkJoinTask<?> pollSubmission()
```
Removes and returns the next unexecuted submission if one is
available. This method may be useful in extensions to this
class that re-assign work in systems with multiple pools.
Returns:
the next submission, or `null` if none

