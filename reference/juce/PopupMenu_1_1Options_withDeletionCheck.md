#### withDeletionCheck()


 Options PopupMenu::Options::withDeletionCheck ( Component & componentToWatchForDeletion ) const nodiscard 
 

If the passed component has been deleted when the popup menu exits, the selected item's action will not be called.This is useful for avoiding dangling references inside the action callback, in the case that the callback needs to access a component that may be deleted.