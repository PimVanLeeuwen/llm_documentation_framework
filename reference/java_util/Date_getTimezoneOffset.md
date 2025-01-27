#### getTimezoneOffset

```
@Deprecated
public int getTimezoneOffset()
```
Deprecated. As of JDK version 1.1,
replaced by `-(Calendar.get(Calendar.ZONE_OFFSET) +
Calendar.get(Calendar.DST_OFFSET)) / (60 * 1000)`.
Returns the offset, measured in minutes, for the local time zone
relative to UTC that is appropriate for the time represented by
this `Date` object.For example, in Massachusetts, five time zones west of Greenwich:
```

 new Date(96, 1, 14).getTimezoneOffset() returns 300
```
because on February 14, 1996, standard time (Eastern Standard Time)
is in use, which is offset five hours from UTC; but:
```

 new Date(96, 5, 1).getTimezoneOffset() returns 240
```
because on June 1, 1996, daylight saving time (Eastern Daylight Time)
is in use, which is offset only four hours from UTC.This method produces the same result as if it computed:
```

 (this.getTime() - UTC(this.getYear(),
                       this.getMonth(),
                       this.getDate(),
                       this.getHours(),
                       this.getMinutes(),
                       this.getSeconds())) / (60 * 1000)
 
```

Returns:
the time-zone offset, in minutes, for the current time zone.
See Also:
`Calendar.ZONE_OFFSET`,
`Calendar.DST_OFFSET`,
`TimeZone.getDefault()`

