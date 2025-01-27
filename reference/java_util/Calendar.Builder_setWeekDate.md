#### setWeekDate

```
public Calendar.Builder setWeekDate(int weekYear,
                                    int weekOfYear,
                                    int dayOfWeek)
```
Sets the week-based date parameters to the values with the given
date specifiers - week year, week of year, and day of week.If the specified calendar doesn't support week dates, the
`build` method will throw an `IllegalArgumentException`.
Parameters:
`weekYear` - the week year
`weekOfYear` - the week number based on `weekYear`
`dayOfWeek` - the day of week value: one of the constants
for the `DAY_OF_WEEK` field:
`SUNDAY`, ..., `SATURDAY`.
Returns:
this `Calendar.Builder`
See Also:
`Calendar.setWeekDate(int, int, int)`,
`Calendar.isWeekDateSupported()`

