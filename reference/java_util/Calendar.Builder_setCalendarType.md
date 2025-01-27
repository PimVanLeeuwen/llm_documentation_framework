#### setCalendarType

```
public Calendar.Builder setCalendarType(String type)
```
Sets the calendar type parameter to the given `type`. The
calendar type given by this method has precedence over any explicit
or implicit calendar type given by the
locale.In addition to the available calendar types returned by the
`Calendar.getAvailableCalendarTypes`
method, `"gregorian"` and `"iso8601"` as aliases of
`"gregory"` can be used with this method.
Parameters:
`type` - the calendar type
Returns:
this `Calendar.Builder`
Throws:
`NullPointerException` - if `type` is `null`
`IllegalArgumentException` - if `type` is unknown
`IllegalStateException` - if another calendar type has already been set
See Also:
`Calendar.getCalendarType()`,
`Calendar.getAvailableCalendarTypes()`

