```
public interface PreferencesFactory
```
A factory object that generates Preferences objects. Providers of
new `Preferences` implementations should provide corresponding
PreferencesFactory implementations so that the new
Preferences implementation can be installed in place of the
platform-specific default implementation.This class is for Preferences implementers only.
Normal users of the Preferences facility should have no need to
consult this documentation.
Since:
1.4
See Also:
`Preferences`
