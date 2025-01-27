#### getAvailableLocales

```
public static Locale[] getAvailableLocales()
```
Returns an array of all locales for which the `getInstance`
methods of this class can return localized instances.
The array returned must contain at least a `Locale`
instance equal to `Locale.US`.
Returns:
An array of locales for which localized
`Calendar` instances are available.

