#### setExecuteExistingDelayedTasksAfterShutdownPolicy

```
public void setExecuteExistingDelayedTasksAfterShutdownPolicy(boolean value)
```
Sets the policy on whether to execute existing delayed
tasks even when this executor has been `shutdown`.
In this case, these tasks will only terminate upon
`shutdownNow`, or after setting the policy to
`false` when already shutdown.
This value is by default `true`.
Parameters:
`value` - if `true`, execute after shutdown, else don't
See Also:
`getExecuteExistingDelayedTasksAfterShutdownPolicy()`

