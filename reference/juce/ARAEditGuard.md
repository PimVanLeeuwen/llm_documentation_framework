Reference counting helper class to ensure that the DocumentController is in editable state.When adding, removing or modifying ARA model objects the enclosing DocumentController must be in editable state.You can achieve this by using the ARA Library calls ARA::Host::DocumentController::beginEditing() and ARA::Host::DocumentController::endEditing().However, putting the DocumentController in and out of editable state is a potentially costly operation, thus it makes sense to group multiple modifications together and change the editable state only once.ARAEditGuard keeps track of all scopes that want to edit a particular DocumentController and will trigger beginEditing() and endEditing() only for the outermost scope. This allows you to merge multiple editing operations into one by putting ARAEditGuard in their enclosing scope.

Constructor & Destructor Documentation


◆ ARAEditGuard()


 ARAEditGuard::ARAEditGuard ( ARA::Host::DocumentController & dcIn ) explicit 
 



◆ ~ARAEditGuard()


 ARAEditGuard::~ARAEditGuard ( ) 
 