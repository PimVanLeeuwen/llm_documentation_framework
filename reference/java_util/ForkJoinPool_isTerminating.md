#### isTerminating

```
public boolean isTerminating()
```
Returns `true` if the process of termination has
commenced but not yet completed. This method may be useful for
debugging. A return of `true` reported a sufficient
period after shutdown may indicate that submitted tasks have
ignored or suppressed interruption, or are waiting for I/O,
causing this executor not to properly terminate. (See the
advisory notes for class `ForkJoinTask` stating that
tasks should not normally entail blocking operations. But if
they do, they must abort them on interrupt.)
Returns:
`true` if terminating but not yet terminated

