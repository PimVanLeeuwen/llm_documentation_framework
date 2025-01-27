#### setLastAccessTime

```
public ZipEntry setLastAccessTime(FileTime time)
```
Sets the last access time of the entry.If set, the last access time will be stored into the extended
timestamp fields of entry's `optional extra data`, when output
to a ZIP file or ZIP file formatted stream.
Parameters:
`time` - The last access time of the entry
Returns:
This zip entry
Throws:
`NullPointerException` - if the `time` is null
Since:
1.8
See Also:
`getLastAccessTime()`

