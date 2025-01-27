#### save

```
@Deprecated
public void save(OutputStream out,
                             String comments)
```
Deprecated. This method does not throw an IOException if an I/O error
occurs while saving the property list. The preferred way to save a
properties list is via the `store(OutputStream out,
String comments)` method or the
`storeToXML(OutputStream os, String comment)` method.
Calls the `store(OutputStream out, String comments)` method
and suppresses IOExceptions that were thrown.
Parameters:
`out` - an output stream.
`comments` - a description of the property list.
Throws:
`ClassCastException` - if this `Properties` object
contains any keys or values that are not
`Strings`.

