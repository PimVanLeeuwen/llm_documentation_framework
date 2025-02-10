#### sortSubItems()


template<class ElementComparator > 

 void TreeViewItem::sortSubItems ( ElementComparator & comparator ) 
 

Sorts the list of subitems using a standard array comparator.This will use a comparator object to sort the elements into order. The comparator object must have a method of the form:int compareElements (TreeViewItem\* first, TreeViewItem\* second);
TreeViewItemAn item in a TreeView.Definition juce\_TreeView.h:60
..and this method must return:a value of < 0 if the first comes before the seconda value of 0 if the two objects are equivalenta value of > 0 if the second comes before the firstTo improve performance, the compareElements() method can be declared as static or const.