#### roll

```
public void roll(int field,
                 int amount)
```
Adds the specified (signed) amount to the specified calendar field
without changing larger fields. A negative amount means to roll
down.NOTE: This default implementation on `Calendar` just repeatedly calls the
version of `roll()` that rolls by one unit. This may not
always do the right thing. For example, if the `DAY_OF_MONTH` field is 31,
rolling through February will leave it set to 28. The `GregorianCalendar`
version of this function takes care of this problem. Other subclasses
should also provide overrides of this function that do the right thing.
Parameters:
`field` - the calendar field.
`amount` - the signed amount to add to the calendar `field`.
Since:
1.2
See Also:
`roll(int,boolean)`,
`add(int,int)`,
`set(int,int)`

