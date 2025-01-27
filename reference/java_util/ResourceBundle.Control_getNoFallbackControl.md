#### getNoFallbackControl

```
public static final ResourceBundle.Control getNoFallbackControl(List<String> formats)
```
Returns a `ResourceBundle.Control` in which the `getFormats` method returns the specified
`formats` and the `getFallbackLocale`
method returns `null`. The `formats` must
be equal to one of `FORMAT_PROPERTIES`, `FORMAT_CLASS` or `FORMAT_DEFAULT`.
`ResourceBundle.Control` instances returned by this
method are singletons and thread-safe.
Parameters:
`formats` - the formats to be returned by the
`ResourceBundle.Control.getFormats` method
Returns:
a `ResourceBundle.Control` supporting the
specified `formats` with no fallback
`Locale` support
Throws:
`NullPointerException` - if `formats` is `null`
`IllegalArgumentException` - if `formats` is unknown

