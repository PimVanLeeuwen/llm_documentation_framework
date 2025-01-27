#### clear

```
public final void clear(int field)
```
Sets the given calendar field value and the time value
(millisecond offset from the Epoch) of
this `Calendar` undefined. This means that `isSet(field)` will return `false`, and
the date and time calculations will treat the field as if it
had never been set. A `Calendar` implementation
class may use the field's specific default value for date and
time calculations.The `HOUR_OF_DAY`, `HOUR` and `AM_PM`
fields are handled independently and the the resolution rule for the time of
day is applied. Clearing one of the fields doesn't reset
the hour of day value of this `Calendar`. Use `set(Calendar.HOUR_OF_DAY, 0)` to reset the hour
value.
Parameters:
`field` - the calendar field to be cleared.
See Also:
`clear()`

