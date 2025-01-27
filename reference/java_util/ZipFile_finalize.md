#### finalize

```
protected void finalize()
                 throws IOException
```
Ensures that the system resources held by this ZipFile object are
released when there are no more references to it.Since the time when GC would invoke this method is undetermined,
it is strongly recommended that applications invoke the `close`
method as soon they have finished accessing this `ZipFile`.
This will prevent holding up system resources for an undetermined
length of time.
Overrides:
`finalize` in class `Object`
Throws:
`IOException` - if an I/O error has occurred
See Also:
`close()`




