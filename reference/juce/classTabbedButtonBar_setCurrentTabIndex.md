#### setCurrentTabIndex()


 void TabbedButtonBar::setCurrentTabIndex ( int newTabIndex, 
 
 bool sendChangeMessage = true ) 

Changes the currently selected tab.This will send a change message and cause a synchronous callback to the currentTabChanged() method. (But if the given tab is already selected, nothing will be done).To deselect all the tabs, use an index of 1.