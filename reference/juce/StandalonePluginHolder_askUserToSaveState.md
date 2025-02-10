#### askUserToSaveState()


 void StandalonePluginHolder::askUserToSaveState ( const String & fileSuffix = String() ) 
 

Pops up a dialog letting the user save the processor's state to a file.References FileBrowserComponent::canSelectFiles, MemoryBlock::getData(), getFilePatterns(), getLastFile(), FileChooser::getResult(), MemoryBlock::getSize(), AudioProcessor::getStateInformation(), FileChooser::launchAsync(), MessageBoxOptions::makeOptionsOk(), messageBox, processor, File::replaceWithData(), FileBrowserComponent::saveMode, setLastFile(), AlertWindow::showScopedAsync(), stateFileChooser, TRANS, FileBrowserComponent::warnAboutOverwriting, and AlertWindow::WarningIcon.Referenced by StandaloneFilterWindow::handleMenuResult().