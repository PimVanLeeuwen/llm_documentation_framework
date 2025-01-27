#### clearCache

```
public static final void clearCache(ClassLoader loader)
```
Removes all resource bundles from the cache that have been loaded
using the given class loader.
Parameters:
`loader` - the class loader
Throws:
`NullPointerException` - if `loader` is null
Since:
1.6
See Also:
`ResourceBundle.Control.getTimeToLive(String,Locale)`

