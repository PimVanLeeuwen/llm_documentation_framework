#### setMethod

```
public void setMethod(int method)
```
Sets the default compression method for subsequent entries. This
default will be used whenever the compression method is not specified
for an individual ZIP file entry, and is initially set to DEFLATED.
Parameters:
`method` - the default compression method
Throws:
`IllegalArgumentException` - if the specified compression method
is invalid

