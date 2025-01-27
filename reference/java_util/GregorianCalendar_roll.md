#### roll

```
public void roll(int field,
                 int amount)
```
Adds a signed amount to the specified calendar field without changing larger fields.
A negative roll amount means to subtract from field without changing
larger fields. If the specified amount is 0, this method performs nothing.This method calls `Calendar.complete()` before adding the
amount so that all the calendar fields are normalized. If there
is any calendar field having an out-of-range value in non-lenient mode, then an
`IllegalArgumentException` is thrown.Example: Consider a `GregorianCalendar`
originally set to August 31, 1999. Calling `roll(Calendar.MONTH,
8)` sets the calendar to April 30, 1999. Using a
`GregorianCalendar`, the `DAY_OF_MONTH` field cannot
be 31 in the month April. `DAY_OF_MONTH` is set to the closest possible
value, 30. The `YEAR` field maintains the value of 1999 because it
is a larger field than `MONTH`.Example: Consider a `GregorianCalendar`
originally set to Sunday June 6, 1999. Calling
`roll(Calendar.WEEK_OF_MONTH, -1)` sets the calendar to
Tuesday June 1, 1999, whereas calling
`add(Calendar.WEEK_OF_MONTH, -1)` sets the calendar to
Sunday May 30, 1999. This is because the roll rule imposes an
additional constraint: The `MONTH` must not change when the
`WEEK_OF_MONTH` is rolled. Taken together with add rule 1,
the resultant date must be between Tuesday June 1 and Saturday June
5. According to add rule 2, the `DAY_OF_WEEK`, an invariant
when changing the `WEEK_OF_MONTH`, is set to Tuesday, the
closest possible value to Sunday (where Sunday is the first day of the
week).
Overrides:
`roll` in class `Calendar`
Parameters:
`field` - the calendar field.
`amount` - the signed amount to add to `field`.
Throws:
`IllegalArgumentException` - if `field` is
`ZONE_OFFSET`, `DST_OFFSET`, or unknown,
or if any calendar fields have out-of-range values in
non-lenient mode.
Since:
1.2
See Also:
`roll(int,boolean)`,
`add(int,int)`,
`Calendar.set(int,int)`

