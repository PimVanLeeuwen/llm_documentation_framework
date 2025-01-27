#### setCreationTime

```
public ZipEntry setCreationTime(FileTime time)
```
Sets the creation time of the entry.If set, the creation time will be stored into the extended
timestamp fields of entry's `optional extra data`, when
output to a ZIP file or ZIP file formatted stream.
Parameters:
`time` - The creation time of the entry
Returns:
This zip entry
Throws:
`NullPointerException` - if the `time` is null
Since:
1.8
See Also:
`getCreationTime()`

