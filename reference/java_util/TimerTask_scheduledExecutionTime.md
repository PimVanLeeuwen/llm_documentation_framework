#### scheduledExecutionTime

```
public long scheduledExecutionTime()
```
Returns the scheduled execution time of the most recent
actual execution of this task. (If this method is invoked
while task execution is in progress, the return value is the scheduled
execution time of the ongoing task execution.)This method is typically invoked from within a task's run method, to
determine whether the current execution of the task is sufficiently
timely to warrant performing the scheduled activity:
```

   public void run() {
       if (System.currentTimeMillis() - scheduledExecutionTime() >=
           MAX_TARDINESS)
               return;  // Too late; skip this execution.
       // Perform the task
   }
 
```
This method is typically not used in conjunction with
fixed-delay execution repeating tasks, as their scheduled
execution times are allowed to drift over time, and so are not terribly
significant.
Returns:
the time at which the most recent execution of this task was
scheduled to occur, in the format returned by Date.getTime().
The return value is undefined if the task has yet to commence
its first execution.
See Also:
`Date.getTime()`




