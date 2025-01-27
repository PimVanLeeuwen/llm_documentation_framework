#### useLocale

```
public Scanner useLocale(Locale locale)
```
Sets this scanner's locale to the specified locale.A scanner's locale affects many elements of its default
primitive matching regular expressions; see
localized numbers above.Invoking the `reset()` method will set the scanner's locale to
the initial locale.
Parameters:
`locale` - A string specifying the locale to use
Returns:
this scanner

