#### isCommandDown()


 bool ModifierKeys::isCommandDown ( ) const noexcept 
 

Checks whether the 'command' key flag is set (or 'ctrl' on Windows/Linux).This is a platformagnostic way of checking for the operating system's preferred commandkey modifier so on the Mac it tests for the cmd key, on Windows/Linux, it's actually checking for the CTRL key.Referenced by SelectedItemSet< SelectableItemType >::addToSelectionBasedOnModifiers(), and LassoComponent< SelectableItemType >::dragLasso().