#### build

```
public Calendar build()
```
Returns a `Calendar` built from the parameters set by the
setter methods. The calendar type given by the `setCalendarType` method or the locale is
used to determine what `Calendar` to be created. If no explicit
calendar type is given, the locale's default calendar is created.If the calendar type is `"iso8601"`, the
Gregorian change date
of a `GregorianCalendar` is set to `Date(Long.MIN_VALUE)`
to be the proleptic Gregorian calendar. Its week definition
parameters are also set to be compatible
with the ISO 8601 standard. Note that the
`getCalendarType` method of
a `GregorianCalendar` created with `"iso8601"` returns
`"gregory"`.The default values are used for locale and time zone if these
parameters haven't been given explicitly.Any out of range field values are either normalized in lenient
mode or detected as an invalid value in non-lenient mode.
Returns:
a `Calendar` built with parameters of this `Calendar.Builder`
Throws:
`IllegalArgumentException` - if the calendar type is unknown, or
if any invalid field values are given in non-lenient mode, or
if a week date is given for the calendar type that doesn't
support week dates.
See Also:
`Calendar.getInstance(TimeZone, Locale)`,
`Locale.getDefault(Locale.Category)`,
`TimeZone.getDefault()`




