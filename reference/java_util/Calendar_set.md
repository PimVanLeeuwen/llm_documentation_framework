#### set

```
public final void set(int year,
                      int month,
                      int date,
                      int hourOfDay,
                      int minute,
                      int second)
```
Sets the values for the fields `YEAR`, `MONTH`,
`DAY_OF_MONTH`, `HOUR_OF_DAY`, `MINUTE`, and
`SECOND`.
Previous values of other fields are retained. If this is not desired,
call `clear()` first.
Parameters:
`year` - the value used to set the `YEAR` calendar field.
`month` - the value used to set the `MONTH` calendar field.
Month value is 0-based. e.g., 0 for January.
`date` - the value used to set the `DAY_OF_MONTH` calendar field.
`hourOfDay` - the value used to set the `HOUR_OF_DAY` calendar field.
`minute` - the value used to set the `MINUTE` calendar field.
`second` - the value used to set the `SECOND` calendar field.
See Also:
`set(int,int)`,
`set(int,int,int)`,
`set(int,int,int,int,int)`

