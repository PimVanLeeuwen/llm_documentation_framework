#### createCoalescedAction()


 virtual UndoableAction \* UndoableAction::createCoalescedAction ( UndoableAction \* nextAction ) virtual 
 

Allows multiple actions to be coalesced into a single action object, to reduce storage space.If possible, this method should create and return a single action that does the same job as this one followed by the supplied action.If it's not possible to merge the two actions, the method should return a nullptr.