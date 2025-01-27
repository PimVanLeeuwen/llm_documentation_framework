#### getBaseBundleName

```
public String getBaseBundleName()
```
Returns the base name of this bundle, if known, or `null` if unknown.
If not null, then this is the value of the `baseName` parameter
that was passed to the `ResourceBundle.getBundle(...)` method
when the resource bundle was loaded.
Returns:
The base name of the resource bundle, as provided to and expected
by the `ResourceBundle.getBundle(...)` methods.
Since:
1.8
See Also:
`getBundle(java.lang.String, java.util.Locale, java.lang.ClassLoader)`

