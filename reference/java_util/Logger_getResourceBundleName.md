#### getResourceBundleName

```
public String getResourceBundleName()
```
Retrieve the localization resource bundle name for this
logger.
This is either the name specified through the `getLogger` factory method,
or the base name of the
ResourceBundle set through `setResourceBundle` method.
Note that if the result is `null`, then the Logger will use a resource
bundle or resource bundle name inherited from its parent.
Returns:
localization bundle name (may be `null`)

