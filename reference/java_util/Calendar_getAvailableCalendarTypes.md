#### getAvailableCalendarTypes

```
public static Set<String> getAvailableCalendarTypes()
```
Returns an unmodifiable `Set` containing all calendar types
supported by `Calendar` in the runtime environment. The available
calendar types can be used for the Unicode locale extensions.
The `Set` returned contains at least `"gregory"`. The
calendar types don't include aliases, such as `"gregorian"` for
`"gregory"`.
Returns:
an unmodifiable `Set` containing all available calendar types
Since:
1.8
See Also:
`getCalendarType()`,
`Calendar.Builder.setCalendarType(String)`,
`Locale.getUnicodeLocaleType(String)`

