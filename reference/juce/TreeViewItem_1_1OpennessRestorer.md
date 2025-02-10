This handy class takes a copy of a TreeViewItem's openness when you create it, and restores that openness state when its destructor is called.This can very handy when you're refreshing subitems e.g.void MyTreeViewItem::updateChildItems()
{
 OpennessRestorer openness (\*this); // saves the openness state here..
 
 clearSubItems();
 
 // add a bunch of subitems here which may or may not be the same as the ones that
 // were previously there
 addSubItem (...
 
 // ..and at this point, the old openness is restored, so any items that haven't
 // changed will have their old openness retained.
}
TreeViewItem::OpennessRestorerThis handy class takes a copy of a TreeViewItem's openness when you create it, and restores that open...Definition juce\_TreeView.h:608
TreeViewItem::clearSubItemsvoid clearSubItems()Removes any subitems.
TreeViewItem::addSubItemvoid addSubItem(TreeViewItem \*newItem, int insertPosition=1)Adds a subitem.
 

Constructor & Destructor Documentation


◆ OpennessRestorer()


 TreeViewItem::OpennessRestorer::OpennessRestorer ( TreeViewItem & ) 
 



◆ ~OpennessRestorer()


 TreeViewItem::OpennessRestorer::~OpennessRestorer ( ) 
 