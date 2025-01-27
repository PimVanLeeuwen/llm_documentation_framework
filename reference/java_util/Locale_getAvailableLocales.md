#### getAvailableLocales

```
public static Locale[] getAvailableLocales()
```
Returns an array of all installed locales.
The returned array represents the union of locales supported
by the Java runtime environment and by installed
`LocaleServiceProvider`
implementations. It must contain at least a `Locale`
instance equal to `Locale.US`.
Returns:
An array of installed locales.

