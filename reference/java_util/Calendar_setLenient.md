#### setLenient

```
public void setLenient(boolean lenient)
```
Specifies whether or not date/time interpretation is to be lenient. With
lenient interpretation, a date such as "February 942, 1996" will be
treated as being equivalent to the 941st day after February 1, 1996.
With strict (non-lenient) interpretation, such dates will cause an exception to be
thrown. The default is lenient.
Parameters:
`lenient` - `true` if the lenient mode is to be turned
on; `false` if it is to be turned off.
See Also:
`isLenient()`,
`DateFormat.setLenient(boolean)`

