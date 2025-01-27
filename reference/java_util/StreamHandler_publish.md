#### publish

```
public void publish(LogRecord record)
```
Format and publish a LogRecord.The StreamHandler first checks if there is an OutputStream
and if the given LogRecord has at least the required log level.
If not it silently returns. If so, it calls any associated
Filter to check if the record should be published. If so,
it calls its Formatter to format the record and then writes
the result to the current output stream.If this is the first LogRecord to be written to a given
OutputStream, the Formatter's "head" string is
written to the stream before the LogRecord is written.
Specified by:
`publish` in class `Handler`
Parameters:
`record` - description of the log event. A null record is
silently ignored and is not published

