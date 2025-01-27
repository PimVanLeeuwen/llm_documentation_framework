#### launchAsync()


 DialogWindow \* DialogWindow::LaunchOptions::launchAsync ( ) 
 

Launches a new modal dialog window.This will create a dialog based on the settings in this structure, launch it modally, and return immediately. The window that is returned will be automatically deleted when the modal state is terminated.When the dialog's close button is clicked, it'll automatically terminate its modal state, but you can also do this programmatically by calling exitModalState (returnValue) on the DialogWindow.If your content component needs to find the dialog window that it is contained in, a quick trick is to do this:if (DialogWindow\* dw = contentComponent>findParentComponentOfClass<DialogWindow>())
 dw>exitModalState (1234);
Component::findParentComponentOfClassTargetClass \* findParentComponentOfClass() constSearches the parent components for a component of a specified class.Definition juce\_Component.h:825
DialogWindowA dialogbox style window.Definition juce\_DialogWindow.h:64
Referenced by StandalonePluginHolder::showAudioSettingsDialog().