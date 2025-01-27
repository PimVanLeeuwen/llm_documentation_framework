#### getTime

```
public long getTime()
```
Returns the last modification time of the entry.If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the `date and time fields` of the zip file entry. The
`default TimeZone` is used
to convert the standard MS-DOS formatted date and time to the
epoch time.
Returns:
The last modification time of the entry in milliseconds
since the epoch, or -1 if not specified
See Also:
`setTime(long)`,
`setLastModifiedTime(FileTime)`

