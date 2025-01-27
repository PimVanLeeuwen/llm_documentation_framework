#### implies

```
public boolean implies(Permission p)
```
Checks if this PropertyPermission object "implies" the specified
permission.More specifically, this method returns true if:p is an instanceof PropertyPermission,p's actions are a subset of this
object's actions, andp's name is implied by this object's
name. For example, "java.\*" implies "java.home".
Overrides:
`implies` in class `BasicPermission`
Parameters:
`p` - the permission to check against.
Returns:
true if the specified permission is implied by this object,
false if not.

