#### getControl

```
public static final ResourceBundle.Control getControl(List<String> formats)
```
Returns a `ResourceBundle.Control` in which the `getFormats` method returns the specified
`formats`. The `formats` must be equal to
one of `FORMAT_PROPERTIES`, `FORMAT_CLASS` or `FORMAT_DEFAULT`. `ResourceBundle.Control`
instances returned by this method are singletons and thread-safe.Specifying `FORMAT_DEFAULT` is equivalent to
instantiating the `ResourceBundle.Control` class,
except that this method returns a singleton.
Parameters:
`formats` - the formats to be returned by the
`ResourceBundle.Control.getFormats` method
Returns:
a `ResourceBundle.Control` supporting the
specified `formats`
Throws:
`NullPointerException` - if `formats` is `null`
`IllegalArgumentException` - if `formats` is unknown

