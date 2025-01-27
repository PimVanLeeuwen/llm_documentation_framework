```
public final class LoggingPermission
extends BasicPermission
```
The permission which the SecurityManager will check when code
that is running with a SecurityManager calls one of the logging
control methods (such as Logger.setLevel).Currently there is only one named LoggingPermission. This is "control"
and it grants the ability to control the logging configuration, for
example by adding or removing Handlers, by adding or removing Filters,
or by changing logging levels.Programmers do not normally create LoggingPermission objects directly.
Instead they are created by the security policy code based on reading
the security policy file.
Since:
1.4
See Also:
`BasicPermission`,
`Permission`,
`Permissions`,
`PermissionCollection`,
`SecurityManager`,
Serialized Form
