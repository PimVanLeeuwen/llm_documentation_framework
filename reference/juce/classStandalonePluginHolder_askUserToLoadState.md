#### askUserToLoadState()


 void StandalonePluginHolder::askUserToLoadState ( const String & fileSuffix = String() ) 
 

Pops up a dialog letting the user reload the processor's state from a file.References FileBrowserComponent::canSelectFiles, MemoryBlock::getData(), getFilePatterns(), getLastFile(), FileChooser::getResult(), MemoryBlock::getSize(), FileChooser::launchAsync(), File::loadFileAsData(), MessageBoxOptions::makeOptionsOk(), messageBox, FileBrowserComponent::openMode, processor, setLastFile(), AudioProcessor::setStateInformation(), AlertWindow::showScopedAsync(), stateFileChooser, TRANS, and AlertWindow::WarningIcon.Referenced by StandaloneFilterWindow::handleMenuResult().