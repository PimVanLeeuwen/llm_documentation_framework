#### getControl

```
ResourceBundle.Control getControl(String baseName)
```
Returns a `ResourceBundle.Control` instance that is used
to handle resource bundle loading for the given `baseName`. This method must return `null` if the given
`baseName` isn't handled by this provider.
Parameters:
`baseName` - the base name of the resource bundle
Returns:
a `ResourceBundle.Control` instance,
or `null` if the given `baseName` is not
applicable to this provider.
Throws:
`NullPointerException` - if `baseName` is `null`




