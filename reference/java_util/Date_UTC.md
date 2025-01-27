#### UTC

```
@Deprecated
public static long UTC(int year,
                                   int month,
                                   int date,
                                   int hrs,
                                   int min,
                                   int sec)
```
Deprecated. As of JDK version 1.1,
replaced by `Calendar.set(year + 1900, month, date,
hrs, min, sec)` or `GregorianCalendar(year + 1900,
month, date, hrs, min, sec)`, using a UTC
`TimeZone`, followed by `Calendar.getTime().getTime()`.
Determines the date and time based on the arguments. The
arguments are interpreted as a year, month, day of the month,
hour of the day, minute within the hour, and second within the
minute, exactly as for the Date constructor with six
arguments, except that the arguments are interpreted relative
to UTC rather than to the local time zone. The time indicated is
returned represented as the distance, measured in milliseconds,
of that time from the epoch (00:00:00 GMT on January 1, 1970).
Parameters:
`year` - the year minus 1900.
`month` - the month between 0-11.
`date` - the day of the month between 1-31.
`hrs` - the hours between 0-23.
`min` - the minutes between 0-59.
`sec` - the seconds between 0-59.
Returns:
the number of milliseconds since January 1, 1970, 00:00:00 GMT for
the date and time specified by the arguments.
See Also:
`Calendar`

