#### setEndRule

```
public void setEndRule(int endMonth,
                       int endDay,
                       int endDayOfWeek,
                       int endTime,
                       boolean after)
```
Sets the daylight saving time end rule to a weekday before or after the given date within
a month, e.g., the first Monday on or after the 8th.
Parameters:
`endMonth` - The daylight saving time ending month. Month is
a `MONTH` field
value (0-based. e.g., 9 for October).
`endDay` - The day of the month on which the daylight saving time ends.
`endDayOfWeek` - The daylight saving time ending day-of-week.
`endTime` - The daylight saving ending time in local wall clock time,
(in milliseconds within the day) which is local daylight
time in this case.
`after` - If true, this rule selects the first `endDayOfWeek` on
or after `endDay`. If false, this rule
selects the last `endDayOfWeek` on or before
`endDay` of the month.
Throws:
`IllegalArgumentException` - the `endMonth`, `endDay`,
`endDayOfWeek`, or `endTime` parameters are out of range
Since:
1.2

