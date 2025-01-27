#### setLastModifiedTime

```
public ZipEntry setLastModifiedTime(FileTime time)
```
Sets the last modification time of the entry.When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's `date and time fields` in `standard
MS-DOS date and time format`), and the extended timestamp fields
in `optional extra data` in UTC time.
Parameters:
`time` - The last modification time of the entry
Returns:
This zip entry
Throws:
`NullPointerException` - if the `time` is null
Since:
1.8
See Also:
`getLastModifiedTime()`

