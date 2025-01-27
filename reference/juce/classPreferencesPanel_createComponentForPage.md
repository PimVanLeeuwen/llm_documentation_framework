#### createComponentForPage()


 virtual Component \* PreferencesPanel::createComponentForPage ( const String & pageName ) pure virtual 
 

Subclasses must override this to return a component for each preferences page.The subclass should return a pointer to a new component representing the named page, which the panel will then display.The panel will delete the component later when the user goes to another page or deletes the panel.