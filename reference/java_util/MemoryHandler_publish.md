#### publish

```
public void publish(LogRecord record)
```
Store a LogRecord in an internal buffer.If there is a Filter, its isLoggable
method is called to check if the given log record is loggable.
If not we return. Otherwise the given record is copied into
an internal circular buffer. Then the record's level property is
compared with the pushLevel. If the given level is
greater than or equal to the pushLevel then push
is called to write all buffered records to the target output
Handler.
Specified by:
`publish` in class `Handler`
Parameters:
`record` - description of the log event. A null record is
silently ignored and is not published

