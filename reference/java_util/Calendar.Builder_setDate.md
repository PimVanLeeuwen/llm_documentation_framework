#### setDate

```
public Calendar.Builder setDate(int year,
                                int month,
                                int dayOfMonth)
```
Sets the date field parameters to the values given by `year`,
`month`, and `dayOfMonth`. This method is equivalent to
a call to:
```

   setFields(Calendar.YEAR, year,
             Calendar.MONTH, month,
             Calendar.DAY_OF_MONTH, dayOfMonth);
```

Parameters:
`year` - the `YEAR` value
`month` - the `MONTH` value
(the month numbering is 0-based).
`dayOfMonth` - the `DAY_OF_MONTH` value
Returns:
this `Calendar.Builder`

