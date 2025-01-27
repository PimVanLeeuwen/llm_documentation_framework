#### compareAndSetForkJoinTaskTag

```
public final boolean compareAndSetForkJoinTaskTag(short e,
                                                  short tag)
```
Atomically conditionally sets the tag value for this task.
Among other applications, tags can be used as visit markers
in tasks operating on graphs, as in methods that check: `if (task.compareAndSetForkJoinTaskTag((short)0, (short)1))`
before processing, otherwise exiting because the node has
already been visited.
Parameters:
`e` - the expected tag value
`tag` - the new tag value
Returns:
`true` if successful; i.e., the current value was
equal to e and is now tag.
Since:
1.8

