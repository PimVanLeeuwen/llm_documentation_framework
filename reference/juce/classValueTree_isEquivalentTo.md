#### isEquivalentTo()


 bool ValueTree::isEquivalentTo ( const ValueTree & ) const 
 

Performs a deep comparison between the properties and children of two trees.If all the properties and children of the two trees are the same (recursively), this returns true. The normal operator==() only checks whether two trees refer to the same shared data structure, so use this method if you need to do a proper value comparison.