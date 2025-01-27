#### getLogger

```
public static Logger getLogger(String name,
                               String resourceBundleName)
```
Find or create a logger for a named subsystem. If a logger has
already been created with the given name it is returned. Otherwise
a new logger is created.If a new logger is created its log level will be configured
based on the LogManager and it will configured to also send logging
output to its parent's Handlers. It will be registered in
the LogManager global namespace.Note: The LogManager may only retain a weak reference to the newly
created Logger. It is important to understand that a previously
created Logger with the given name may be garbage collected at any
time if there is no strong reference to the Logger. In particular,
this means that two back-to-back calls like
`getLogger("MyLogger", ...).log(...)` may use different Logger
objects named "MyLogger" if there is no strong reference to the
Logger named "MyLogger" elsewhere in the program.If the named Logger already exists and does not yet have a
localization resource bundle then the given resource bundle
name is used. If the named Logger already exists and has
a different resource bundle name then an IllegalArgumentException
is thrown.
Parameters:
`name` - A name for the logger. This should
be a dot-separated name and should normally
be based on the package name or class name
of the subsystem, such as java.net
or javax.swing
`resourceBundleName` - name of ResourceBundle to be used for localizing
messages for this logger. May be `null`
if none of the messages require localization.
Returns:
a suitable Logger
Throws:
`MissingResourceException` - if the resourceBundleName is non-null and
no corresponding resource can be found.
`IllegalArgumentException` - if the Logger already exists and uses
a different resource bundle name; or if
`resourceBundleName` is `null` but the named
logger has a resource bundle set.
`NullPointerException` - if the name is null.

