Contains cached information about one of the files in a DirectoryContentsList.

Member Data Documentation


◆ filename


 String DirectoryContentsList::FileInfo::filename 
 

The filename.This isn't a full pathname, it's just the last part of the path, same as you'd get from File::getFileName().To get the full pathname, use DirectoryContentsList::getDirectory().getChildFile (filename).

◆ fileSize


 int64 DirectoryContentsList::FileInfo::fileSize 
 

File size in bytes.

◆ modificationTime


 Time DirectoryContentsList::FileInfo::modificationTime 
 

File modification time.As supplied by File::getLastModificationTime().

◆ creationTime


 Time DirectoryContentsList::FileInfo::creationTime 
 

File creation time.As supplied by File::getCreationTime().

◆ isDirectory


 bool DirectoryContentsList::FileInfo::isDirectory 
 

True if the file is a directory.

◆ isReadOnly


 bool DirectoryContentsList::FileInfo::isReadOnly 
 

True if the file is readonly.

The documentation for this struct was generated from the following file:juce\_DirectoryContentsList.h
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