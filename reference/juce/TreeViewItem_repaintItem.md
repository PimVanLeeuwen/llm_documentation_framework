#### repaintItem()


 void TreeViewItem::repaintItem ( ) const 
 

Sends a repaint message to redraw just this item.Note that you should only call this if you want to repaint a superficial change. If you're altering the tree's nodes, you should instead call treeHasChanged().