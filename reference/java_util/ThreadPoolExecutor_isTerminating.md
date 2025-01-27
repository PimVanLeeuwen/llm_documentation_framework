#### isTerminating

```
public boolean isTerminating()
```
Returns true if this executor is in the process of terminating
after `shutdown()` or `shutdownNow()` but has not
completely terminated. This method may be useful for
debugging. A return of `true` reported a sufficient
period after shutdown may indicate that submitted tasks have
ignored or suppressed interruption, causing this executor not
to properly terminate.
Returns:
`true` if terminating but not yet terminated

