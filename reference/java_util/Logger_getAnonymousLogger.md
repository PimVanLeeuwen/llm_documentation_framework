#### getAnonymousLogger

```
public static Logger getAnonymousLogger(String resourceBundleName)
```
Create an anonymous Logger. The newly created Logger is not
registered in the LogManager namespace. There will be no
access checks on updates to the logger.This factory method is primarily intended for use from applets.
Because the resulting Logger is anonymous it can be kept private
by the creating class. This removes the need for normal security
checks, which in turn allows untrusted applet code to update
the control state of the Logger. For example an applet can do
a setLevel or an addHandler on an anonymous Logger.Even although the new logger is anonymous, it is configured
to have the root logger ("") as its parent. This means that
by default it inherits its effective level and handlers
from the root logger. Changing its parent via the
`setParent` method
will still require the security permission specified by that method.
Parameters:
`resourceBundleName` - name of ResourceBundle to be used for localizing
messages for this logger.
May be null if none of the messages require localization.
Returns:
a newly created private Logger
Throws:
`MissingResourceException` - if the resourceBundleName is non-null and
no corresponding resource can be found.

