#### setTimeZone

```
public Calendar.Builder setTimeZone(TimeZone zone)
```
Sets the time zone parameter to the given `zone`. If no time
zone parameter is given to this `Caledar.Builder`, the
default
`TimeZone` will be used in the `build`
method.
Parameters:
`zone` - the `TimeZone`
Returns:
this `Calendar.Builder`
Throws:
`NullPointerException` - if `zone` is `null`
See Also:
`Calendar.setTimeZone(TimeZone)`

