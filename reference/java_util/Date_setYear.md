#### setYear

```
@Deprecated
public void setYear(int year)
```
Deprecated. As of JDK version 1.1,
replaced by `Calendar.set(Calendar.YEAR, year + 1900)`.
Sets the year of this Date object to be the specified
value plus 1900. This `Date` object is modified so
that it represents a point in time within the specified year,
with the month, date, hour, minute, and second the same as
before, as interpreted in the local time zone. (Of course, if
the date was February 29, for example, and the year is set to a
non-leap year, then the new date will be treated as if it were
on March 1.)
Parameters:
`year` - the year value.
See Also:
`Calendar`

