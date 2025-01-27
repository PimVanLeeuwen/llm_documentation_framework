#### systemNodeForPackage

```
public static Preferences systemNodeForPackage(Class<?> c)
```
Returns the preference node from the system preference tree that is
associated (by convention) with the specified class's package. The
convention is as follows: the absolute path name of the node is the
fully qualified package name, preceded by a slash ('/'), and
with each period ('.') replaced by a slash. For example the
absolute path name of the node associated with the class
com.acme.widget.Foo is /com/acme/widget.This convention does not apply to the unnamed package, whose
associated preference node is <unnamed>. This node
is not intended for long term use, but for convenience in the early
development of programs that do not yet belong to a package, and
for "throwaway" programs. Valuable data should not be stored
at this node as it is shared by all programs that use it.A class Foo wishing to access preferences pertaining to its
package can obtain a preference node as follows:
```

  static Preferences prefs = Preferences.systemNodeForPackage(Foo.class);
 
```
This idiom obviates the need for using a string to describe the
preferences node and decreases the likelihood of a run-time failure.
(If the class name is misspelled, it will typically result in a
compile-time error.)Invoking this method will result in the creation of the returned
node and its ancestors if they do not already exist. If the returned
node did not exist prior to this call, this node and any ancestors that
were created by this call are not guaranteed to become permanent until
the flush method is called on the returned node (or one of its
ancestors or descendants).
Parameters:
`c` - the class for whose package a system preference node is desired.
Returns:
the system preference node associated with the package of which
c is a member.
Throws:
`NullPointerException` - if c is null.
`SecurityException` - if a security manager is present and
it denies RuntimePermission("preferences").
See Also:
`RuntimePermission`

