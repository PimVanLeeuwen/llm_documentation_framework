#### addAction()


 AccessibilityActions & AccessibilityActions::addAction ( AccessibilityActionType type, 
 
 std::function< void()> actionCallback ) 

Adds an action.When the user performs this action with an accessibility client `actionCallback` will be called.Returns a reference to itself so that several calls can be chained.