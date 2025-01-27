#### schedule

```
public void schedule(TimerTask task,
                     Date firstTime,
                     long period)
```
Schedules the specified task for repeated fixed-delay execution,
beginning at the specified time. Subsequent executions take place at
approximately regular intervals, separated by the specified period.In fixed-delay execution, each execution is scheduled relative to
the actual execution time of the previous execution. If an execution
is delayed for any reason (such as garbage collection or other
background activity), subsequent executions will be delayed as well.
In the long run, the frequency of execution will generally be slightly
lower than the reciprocal of the specified period (assuming the system
clock underlying Object.wait(long) is accurate). As a
consequence of the above, if the scheduled first time is in the past,
it is scheduled for immediate execution.Fixed-delay execution is appropriate for recurring activities
that require "smoothness." In other words, it is appropriate for
activities where it is more important to keep the frequency accurate
in the short run than in the long run. This includes most animation
tasks, such as blinking a cursor at regular intervals. It also includes
tasks wherein regular activity is performed in response to human
input, such as automatically repeating a character as long as a key
is held down.
Parameters:
`task` - task to be scheduled.
`firstTime` - First time at which task is to be executed.
`period` - time in milliseconds between successive task executions.
Throws:
`IllegalArgumentException` - if `firstTime.getTime() < 0`, or
`period <= 0`
`IllegalStateException` - if task was already scheduled or
cancelled, timer was cancelled, or timer thread terminated.
`NullPointerException` - if `task` or `firstTime` is null

