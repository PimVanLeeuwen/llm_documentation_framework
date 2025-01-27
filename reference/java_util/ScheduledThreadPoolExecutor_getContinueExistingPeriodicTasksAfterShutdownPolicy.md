#### getContinueExistingPeriodicTasksAfterShutdownPolicy

```
public boolean getContinueExistingPeriodicTasksAfterShutdownPolicy()
```
Gets the policy on whether to continue executing existing
periodic tasks even when this executor has been `shutdown`.
In this case, these tasks will only terminate upon
`shutdownNow` or after setting the policy to
`false` when already shutdown.
This value is by default `false`.
Returns:
`true` if will continue after shutdown
See Also:
`setContinueExistingPeriodicTasksAfterShutdownPolicy(boolean)`

