#### createItemComponent()


 virtual std::unique\_ptr< Component > TreeViewItem::createItemComponent ( ) virtual 
 

Creates a component that will be used to represent this item.You don't have to implement this method if it returns nullptr then no component will be used for the item, and you can just draw it using the paintItem() callback. But if you do return a component, it will be positioned in the TreeView so that it can be used to represent this item.The component returned will be managed by the TreeView and will be deleted later when it goes off the screen or is no longer needed. Its position and size will be completely managed by the tree, so don't attempt to move it around.Something you may want to do with your component is to give it a pointer to the TreeView that created it. This is perfectly safe, and there's no danger of it becoming a dangling pointer because the TreeView will always delete the component before it is itself deleted.As long as you stick to these rules you can return whatever kind of component you like. It's most useful if you're doing things like draganddrop of items, or want to use a Label component to edit item names, etc.