#### getResourceBundle

```
public ResourceBundle getResourceBundle()
```
Retrieve the localization resource bundle for this
logger.
This method will return a `ResourceBundle` that was either
set by the `setResourceBundle` method or
mapped from the
the resource bundle name set via the `getLogger` factory
method for the current default locale.
Note that if the result is `null`, then the Logger will use a resource
bundle or resource bundle name inherited from its parent.
Returns:
localization bundle (may be `null`)

