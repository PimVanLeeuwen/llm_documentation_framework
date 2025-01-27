#### getExecuteExistingDelayedTasksAfterShutdownPolicy

```
public boolean getExecuteExistingDelayedTasksAfterShutdownPolicy()
```
Gets the policy on whether to execute existing delayed
tasks even when this executor has been `shutdown`.
In this case, these tasks will only terminate upon
`shutdownNow`, or after setting the policy to
`false` when already shutdown.
This value is by default `true`.
Returns:
`true` if will execute after shutdown
See Also:
`setExecuteExistingDelayedTasksAfterShutdownPolicy(boolean)`

