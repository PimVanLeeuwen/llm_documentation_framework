#### getDisplayNames

```
public abstract Map<String,Integer> getDisplayNames(String calendarType,
                                                    int field,
                                                    int style,
                                                    Locale locale)
```
Returns a `Map` containing all string representations (display
names) of the `Calendar` `field` in the given `style`
and `locale` and their corresponding field values.`field` is a `Calendar` field index, such as `Calendar.MONTH`. The time zone fields, `Calendar.ZONE_OFFSET` and
`Calendar.DST_OFFSET`, are not supported by this
method. `null` must be returned if any time zone fields are specified.`style` gives the style of the string representation. It must be
one of `Calendar.ALL_STYLES`, `Calendar.SHORT_FORMAT` (`SHORT`), `Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT` (`LONG`), `Calendar.LONG_STANDALONE`, `Calendar.NARROW_FORMAT`, or
`Calendar.NARROW_STANDALONE`. Note that narrow names may
not be unique due to use of single characters, such as "S" for Sunday
and Saturday, and that no narrow names are included in that case.For example, the following call will return a `Map` containing
`"January"` to `Calendar.JANUARY`, `"Jan"` to `Calendar.JANUARY`, `"February"` to `Calendar.FEBRUARY`,
`"Feb"` to `Calendar.FEBRUARY`, and so on.
```

 getDisplayNames("gregory", Calendar.MONTH, Calendar.ALL_STYLES, Locale.ENGLISH);
 
```

Parameters:
`calendarType` - the calendar type. (Any calendar type given by `locale`
is ignored.)
`field` - the calendar field for which the display names are returned
`style` - the style applied to the display names; one of
`Calendar.ALL_STYLES`, `Calendar.SHORT_FORMAT`
(`SHORT`), `Calendar.SHORT_STANDALONE`, `Calendar.LONG_FORMAT`
(`LONG`), `Calendar.LONG_STANDALONE`,
`Calendar.NARROW_FORMAT`,
or `Calendar.NARROW_STANDALONE`
`locale` - the desired locale
Returns:
a `Map` containing all display names of `field` in
`style` and `locale` and their `field` values,
or `null` if no display names are defined for `field`
Throws:
`NullPointerException` - if `locale` is `null`
See Also:
`Calendar.getDisplayNames(int, int, Locale)`




