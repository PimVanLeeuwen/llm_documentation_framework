#### absolutePath

```
public String absolutePath()
```
Implements the absolutePath method as per the specification in
`Preferences.absolutePath()`.This implementation merely returns the absolute path name that
was computed at the time that this node was constructed (based on
the name that was passed to this node's constructor, and the names
that were passed to this node's ancestors' constructors).
Specified by:
`absolutePath` in class `Preferences`
Returns:
this preference node's absolute path name.

