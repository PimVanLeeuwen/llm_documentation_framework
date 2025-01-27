#### getLoggingMXBean

```
public static LoggingMXBean getLoggingMXBean()
```
Returns LoggingMXBean for managing loggers.
An alternative way to manage loggers is through the
`PlatformLoggingMXBean` interface
that can be obtained by calling:
```

     PlatformLoggingMXBean logging = ManagementFactory.getPlatformMXBean(PlatformLoggingMXBean.class);
 
```

Returns:
a `LoggingMXBean` object.
Since:
1.5
See Also:
`PlatformLoggingMXBean`




