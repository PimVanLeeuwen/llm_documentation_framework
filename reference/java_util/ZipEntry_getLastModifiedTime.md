#### getLastModifiedTime

```
public FileTime getLastModifiedTime()
```
Returns the last modification time of the entry.If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's `optional extra data` if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's `date and time fields`, the `default TimeZone` is used to convert
the standard MS-DOS formatted date and time to the epoch time.
Returns:
The last modification time of the entry, null if not specified
Since:
1.8
See Also:
`setLastModifiedTime(FileTime)`

