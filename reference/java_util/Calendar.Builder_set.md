#### set

```
public Calendar.Builder set(int field,
                            int value)
```
Sets the `field` parameter to the given `value`.
`field` is an index to the `Calendar.fields`, such as
`DAY_OF_MONTH`. Field value validation is
not performed in this method. Any out of range values are either
normalized in lenient mode or detected as an invalid value in
non-lenient mode when building a `Calendar`.
Parameters:
`field` - an index to the `Calendar` fields
`value` - the field value
Returns:
this `Calendar.Builder`
Throws:
`IllegalArgumentException` - if `field` is invalid
`IllegalStateException` - if the instant value has already been set,
or if fields have been set too many
(approximately `Integer.MAX_VALUE`) times.
See Also:
`Calendar.set(int, int)`

