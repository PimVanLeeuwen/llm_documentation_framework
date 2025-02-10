#### clearContentComponent()


 void ResizableWindow::clearContentComponent ( ) 
 

Removes the current content component.If the previous content component was added with setContentOwned(), it will also be deleted. If it was added with setContentNonOwned(), it will simply be removed from this component.Referenced by StandaloneFilterWindow::resetToDefaultState(), and StandaloneFilterWindow::~StandaloneFilterWindow().