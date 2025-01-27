```
public final class PropertyPermission
extends BasicPermission
```
This class is for property permissions.The name is the name of the property ("java.home",
"os.name", etc). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "java.\*" and "\*" signify a wildcard
match, while "\*java" and "a\*b" do not.The actions to be granted are passed to the constructor in a string containing
a list of one or more comma-separated keywords. The possible keywords are
"read" and "write". Their meaning is defined as follows:
 read
 read permission. Allows `System.getProperty` to
be called.
 write
 write permission. Allows `System.setProperty` to
be called.
The actions string is converted to lowercase before processing.Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).
Since:
1.2
See Also:
`BasicPermission`,
`Permission`,
`Permissions`,
`PermissionCollection`,
`SecurityManager`
