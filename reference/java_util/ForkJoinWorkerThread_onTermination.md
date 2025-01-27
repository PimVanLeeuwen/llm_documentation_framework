#### onTermination

```
protected void onTermination(Throwable exception)
```
Performs cleanup associated with termination of this worker
thread. If you override this method, you must invoke
`super.onTermination` at the end of the overridden method.
Parameters:
`exception` - the exception causing this thread to abort due
to an unrecoverable error, or `null` if completed normally

