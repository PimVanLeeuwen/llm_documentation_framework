#### addNodeChangeListener

```
public void addNodeChangeListener(NodeChangeListener ncl)
```
Description copied from class: `Preferences`
Registers the specified listener to receive node change events
for this node. A node change event is generated when a child node is
added to or removed from this node. (A single `Preferences.removeNode()`
invocation results in multiple node change events, one for every
node in the subtree rooted at the removed node.)Events are only guaranteed for changes made within the same JVM
as the registered listener, though some implementations may generate
events for changes made outside this JVM. Events may be generated
before the changes have become permanent. Events are not generated
when indirect descendants of this node are added or removed; a
caller desiring such events must register with each descendant.Few guarantees can be made regarding node creation. Because nodes
are created implicitly upon access, it may not be feasible for an
implementation to determine whether a child node existed in the backing
store prior to access (for example, because the backing store is
unreachable or cached information is out of date). Under these
circumstances, implementations are neither required to generate node
change events nor prohibited from doing so.
Specified by:
`addNodeChangeListener` in class `Preferences`
Parameters:
`ncl` - The NodeChangeListener to add.
See Also:
`Preferences.removeNodeChangeListener(NodeChangeListener)`,
`Preferences.addPreferenceChangeListener(PreferenceChangeListener)`

