#### setContinueExistingPeriodicTasksAfterShutdownPolicy

```
public void setContinueExistingPeriodicTasksAfterShutdownPolicy(boolean value)
```
Sets the policy on whether to continue executing existing
periodic tasks even when this executor has been `shutdown`.
In this case, these tasks will only terminate upon
`shutdownNow` or after setting the policy to
`false` when already shutdown.
This value is by default `false`.
Parameters:
`value` - if `true`, continue after shutdown, else don't
See Also:
`getContinueExistingPeriodicTasksAfterShutdownPolicy()`

