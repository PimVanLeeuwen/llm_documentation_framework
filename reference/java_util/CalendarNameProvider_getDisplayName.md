#### getDisplayName

```
public abstract String getDisplayName(String calendarType,
                                      int field,
                                      int value,
                                      int style,
                                      Locale locale)
```
Returns the string representation (display name) of the calendar
`field value` in the given `style` and
`locale`. If no string representation is
applicable, `null` is returned.`field` is a `Calendar` field index, such as `Calendar.MONTH`. The time zone fields, `Calendar.ZONE_OFFSET` and
`Calendar.DST_OFFSET`, are not supported by this
method. `null` must be returned if any time zone fields are
specified.`value` is the numeric representation of the `field` value.
For example, if `field` is `Calendar.DAY_OF_WEEK`, the valid
values are `Calendar.SUNDAY` to `Calendar.SATURDAY`
(inclusive).`style` gives the style of the string representation. It is one
of `Calendar.SHORT_FORMAT` (`SHORT`),
`Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT`
(`LONG`), `Calendar.LONG_STANDALONE`,
`Calendar.NARROW_FORMAT`, or `Calendar.NARROW_STANDALONE`.For example, the following call will return `"Sunday"`.
```

 getDisplayName("gregory", Calendar.DAY_OF_WEEK, Calendar.SUNDAY,
                Calendar.LONG_STANDALONE, Locale.ENGLISH);
 
```

Parameters:
`calendarType` - the calendar type. (Any calendar type given by `locale`
is ignored.)
`field` - the `Calendar` field index,
such as `Calendar.DAY_OF_WEEK`
`value` - the value of the `Calendar field`,
such as `Calendar.MONDAY`
`style` - the string representation style: one of `Calendar.SHORT_FORMAT` (`SHORT`),
`Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT` (`LONG`),
`Calendar.LONG_STANDALONE`,
`Calendar.NARROW_FORMAT`,
or `Calendar.NARROW_STANDALONE`
`locale` - the desired locale
Returns:
the string representation of the `field value`, or `null` if the string representation is not applicable or
the given calendar type is unknown
Throws:
`IllegalArgumentException` - if `field` or `style` is invalid
`NullPointerException` - if `locale` is `null`
See Also:
`TimeZoneNameProvider`,
`Calendar.get(int)`,
`Calendar.getDisplayName(int, int, Locale)`

