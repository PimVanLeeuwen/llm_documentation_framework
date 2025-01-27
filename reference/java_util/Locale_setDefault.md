#### setDefault

```
public static void setDefault(Locale.Category category,
                              Locale newLocale)
```
Sets the default locale for the specified Category for this instance
of the Java Virtual Machine. This does not affect the host locale.If there is a security manager, its checkPermission method is called
with a PropertyPermission("user.language", "write") permission before
the default locale is changed.The Java Virtual Machine sets the default locale during startup based
on the host environment. It is used by many locale-sensitive methods
if no locale is explicitly specified.Since changing the default locale may affect many different areas of
functionality, this method should only be used if the caller is
prepared to reinitialize locale-sensitive code running within the
same Java Virtual Machine.
Parameters:
`category` - - the specified category to set the default locale
`newLocale` - - the new default locale
Throws:
`SecurityException` - - if a security manager exists and its
checkPermission method doesn't allow the operation.
`NullPointerException` - - if category and/or newLocale is null
Since:
1.7
See Also:
`SecurityManager.checkPermission(java.security.Permission)`,
`PropertyPermission`,
`getDefault(Locale.Category)`

