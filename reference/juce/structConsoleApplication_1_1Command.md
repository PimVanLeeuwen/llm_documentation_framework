Represents a command that can be executed if its commandline arguments are matched.See alsoConsoleApplication::addCommand(), ConsoleApplication::findAndRunCommand() 

Member Data Documentation


◆ commandOption


 String ConsoleApplication::Command::commandOption 
 

The option string that must appear in the argument list for this command to be invoked.This can also be a list of different versions separated by pipes, e.g. "helph"

◆ argumentDescription


 String ConsoleApplication::Command::argumentDescription 
 

A description of the commandline arguments needed for this command, which will be printed as part of the help text.

◆ shortDescription


 String ConsoleApplication::Command::shortDescription 
 

A short (one line) description of this command, which can be printed by ConsoleApplication::printCommandList().

◆ longDescription


 String ConsoleApplication::Command::longDescription 
 

A longer description of this command, for use in extended help.

◆ command


 std::function<void (const ArgumentList&)> ConsoleApplication::Command::command 
 

The actual command that should be invoked to perform this action.

The documentation for this struct was generated from the following file:juce\_ConsoleApplication.h
### Purchase

Get JUCE
### Discover

What's New in JUCEFeatures
### Learn

DocumentaionTutorialsMade with JUCEResources
### Support

JUCE ForumNewsletterArchive
### About

Contact UsJUCE LegalJUCE Licensing FAQ
### Events

Audio Developer Conference
Visit our FacebookVisit our TwitterVisit our LinkedInVisit our YouTube channel© Raw Material Software Limited
linkedin




facebook


pinterest


youtube


rss


twitter


instagram




facebookblank


rssblank


linkedinblank


pinterest


youtube


twitter


instagram