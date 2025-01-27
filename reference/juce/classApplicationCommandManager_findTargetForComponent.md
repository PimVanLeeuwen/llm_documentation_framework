#### findTargetForComponent()


 static ApplicationCommandTarget \* ApplicationCommandManager::findTargetForComponent ( Component \* ) static 
 

Examines this component and all its parents in turn, looking for the first one which is an ApplicationCommandTarget.Returns the first ApplicationCommandTarget that it finds, or nullptr if none of them implement that class.