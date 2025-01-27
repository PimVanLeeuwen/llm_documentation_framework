#### setTimeOfDay

```
public Calendar.Builder setTimeOfDay(int hourOfDay,
                                     int minute,
                                     int second,
                                     int millis)
```
Sets the time of day field parameters to the values given by
`hourOfDay`, `minute`, `second`, and
`millis`. This method is equivalent to a call to:
```

   setFields(Calendar.HOUR_OF_DAY, hourOfDay,
             Calendar.MINUTE, minute,
             Calendar.SECOND, second,
             Calendar.MILLISECOND, millis);
```

Parameters:
`hourOfDay` - the `HOUR_OF_DAY` value
(24-hour clock)
`minute` - the `MINUTE` value
`second` - the `SECOND` value
`millis` - the `MILLISECOND` value
Returns:
this `Calendar.Builder`

