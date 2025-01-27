#### setTime

```
public void setTime(long time)
```
Sets the last modification time of the entry.If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the `date and time fields` of the zip file
entry and encoded in standard `MS-DOS date and time format`.
The `default TimeZone` is
used to convert the epoch time to the MS-DOS data and time.
Parameters:
`time` - The last modification time of the entry in milliseconds
since the epoch
See Also:
`getTime()`,
`getLastModifiedTime()`

