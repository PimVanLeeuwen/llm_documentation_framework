#### getActions

```
public String getActions()
```
Returns the "canonical string representation" of the actions.
That is, this method always returns present actions in the following order:
read, write. For example, if this PropertyPermission object
allows both write and read actions, a call to `getActions`
will return the string "read,write".
Overrides:
`getActions` in class `BasicPermission`
Returns:
the canonical string representation of the actions.

