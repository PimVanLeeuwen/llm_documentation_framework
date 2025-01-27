#### build() [2/2]


 Animator ValueAnimatorBuilder::build ( ) && 
 

The build() function will instantiate a new underlying implementation with the specified parameters and return an Animator object referencing it.Calling build() multiple times will return unrelated Animator objects, that reference separate underlying implementation instances.This overload will be called on rvalue handles.