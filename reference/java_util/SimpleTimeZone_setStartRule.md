#### setStartRule

```
public void setStartRule(int startMonth,
                         int startDay,
                         int startDayOfWeek,
                         int startTime,
                         boolean after)
```
Sets the daylight saving time start rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.
Parameters:
`startMonth` - The daylight saving time starting month. Month is
a `MONTH` field
value (0-based. e.g., 0 for January).
`startDay` - The day of the month on which the daylight saving time starts.
`startDayOfWeek` - The daylight saving time starting day-of-week.
`startTime` - The daylight saving time starting time in local wall clock
time, which is local standard time in this case.
`after` - If true, this rule selects the first `dayOfWeek` on or
after `dayOfMonth`. If false, this rule
selects the last `dayOfWeek` on or before
`dayOfMonth`.
Throws:
`IllegalArgumentException` - if the `startMonth`, `startDay`,
`startDayOfWeek`, or `startTime` parameters are out of range
Since:
1.2

