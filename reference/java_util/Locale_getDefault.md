#### getDefault

```
public static Locale getDefault(Locale.Category category)
```
Gets the current value of the default locale for the specified Category
for this instance of the Java Virtual Machine.The Java Virtual Machine sets the default locale during startup based
on the host environment. It is used by many locale-sensitive methods
if no locale is explicitly specified. It can be changed using the
setDefault(Locale.Category, Locale) method.
Parameters:
`category` - - the specified category to get the default locale
Returns:
the default locale for the specified Category for this instance
of the Java Virtual Machine
Throws:
`NullPointerException` - - if category is null
Since:
1.7
See Also:
`setDefault(Locale.Category, Locale)`

