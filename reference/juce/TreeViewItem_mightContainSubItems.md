#### mightContainSubItems()


 virtual bool TreeViewItem::mightContainSubItems ( ) pure virtual 
 

Tells the tree whether this item can potentially be opened.If your item could contain subitems, this should return true; if it returns false then the tree will not try to open the item. This determines whether or not the item will be drawn with a 'plus' button next to it.