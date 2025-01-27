#### scheduleAtFixedRate

```
public void scheduleAtFixedRate(TimerTask task,
                                Date firstTime,
                                long period)
```
Schedules the specified task for repeated fixed-rate execution,
beginning at the specified time. Subsequent executions take place at
approximately regular intervals, separated by the specified period.In fixed-rate execution, each execution is scheduled relative to the
scheduled execution time of the initial execution. If an execution is
delayed for any reason (such as garbage collection or other background
activity), two or more executions will occur in rapid succession to
"catch up." In the long run, the frequency of execution will be
exactly the reciprocal of the specified period (assuming the system
clock underlying Object.wait(long) is accurate). As a
consequence of the above, if the scheduled first time is in the past,
then any "missed" executions will be scheduled for immediate "catch up"
execution.Fixed-rate execution is appropriate for recurring activities that
are sensitive to absolute time, such as ringing a chime every
hour on the hour, or running scheduled maintenance every day at a
particular time. It is also appropriate for recurring activities
where the total time to perform a fixed number of executions is
important, such as a countdown timer that ticks once every second for
ten seconds. Finally, fixed-rate execution is appropriate for
scheduling multiple repeating timer tasks that must remain synchronized
with respect to one another.
Parameters:
`task` - task to be scheduled.
`firstTime` - First time at which task is to be executed.
`period` - time in milliseconds between successive task executions.
Throws:
`IllegalArgumentException` - if `firstTime.getTime() < 0` or
`period <= 0`
`IllegalStateException` - if task was already scheduled or
cancelled, timer was cancelled, or timer thread terminated.
`NullPointerException` - if `task` or `firstTime` is null

