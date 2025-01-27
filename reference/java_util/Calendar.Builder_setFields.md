#### setFields

```
public Calendar.Builder setFields(int... fieldValuePairs)
```
Sets field parameters to their values given by
`fieldValuePairs` that are pairs of a field and its value.
For example,
```

   setFeilds(Calendar.YEAR, 2013,
             Calendar.MONTH, Calendar.DECEMBER,
             Calendar.DAY_OF_MONTH, 23);
```
is equivalent to the sequence of the following
`set` calls:
```

   set(Calendar.YEAR, 2013)
   .set(Calendar.MONTH, Calendar.DECEMBER)
   .set(Calendar.DAY_OF_MONTH, 23);
```

Parameters:
`fieldValuePairs` - field-value pairs
Returns:
this `Calendar.Builder`
Throws:
`NullPointerException` - if `fieldValuePairs` is `null`
`IllegalArgumentException` - if any of fields are invalid,
or if `fieldValuePairs.length` is an odd number.
`IllegalStateException` - if the instant value has been set,
or if fields have been set too many (approximately
`Integer.MAX_VALUE`) times.

