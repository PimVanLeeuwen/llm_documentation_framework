#### compareTo

```
public int compareTo(Calendar anotherCalendar)
```
Compares the time values (millisecond offsets from the Epoch) represented by two
`Calendar` objects.
Specified by:
`compareTo` in interface `Comparable<Calendar>`
Parameters:
`anotherCalendar` - the `Calendar` to be compared.
Returns:
the value `0` if the time represented by the argument
is equal to the time represented by this `Calendar`; a value
less than `0` if the time of this `Calendar` is
before the time represented by the argument; and a value greater than
`0` if the time of this `Calendar` is after the
time represented by the argument.
Throws:
`NullPointerException` - if the specified `Calendar` is
`null`.
`IllegalArgumentException` - if the time value of the
specified `Calendar` object can't be obtained due to
any invalid calendar values.
Since:
1.5

