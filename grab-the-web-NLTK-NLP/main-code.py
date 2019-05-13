# -*- coding: utf-8 -*-
"""
Created on Mon May 13 04:09:31 2019

@author: wrm
"""

from bs4 import BeautifulSoup
import urllib
response=urllib.urlopen("http://php.net/")
"""
print (response)
<http.client.HTTPResponse object at 0x0000026437EEAE10>
"""
html=response.read()
#print (html)
soup=BeautifulSoup(html,"html5lib")
#print (soup)
text=soup.get_text(strip=True)
#print (text)

"""
PHP: Hypertext PreprocessorDownloadsDocumentationGet InvolvedHelpGetting StartedIntroductionA simple tutorialLanguage ReferenceBasic syntaxTypesVariablesConstantsExpressionsOperatorsControl StructuresFunctionsClasses and ObjectsNamespacesErrorsExceptionsGeneratorsReferences ExplainedPredefined VariablesPredefined ExceptionsPredefined Interfaces and ClassesContext options and parametersSupported Protocols and WrappersSecurityIntroductionGeneral considerationsInstalled as CGI binaryInstalled as an Apache moduleSession SecurityFilesystem SecurityDatabase SecurityError ReportingUsing Register GlobalsUser Submitted DataMagic QuotesHiding PHPKeeping CurrentFeaturesHTTP authentication with PHPCookiesSessionsDealing with XFormsHandling file uploadsUsing remote filesConnection handlingPersistent Database ConnectionsSafe ModeCommand line usageGarbage CollectionDTrace Dynamic TracingFunction ReferenceAffecting PHP's BehaviourAudio Formats ManipulationAuthentication ServicesCommand Line Specific ExtensionsCompression and Archive ExtensionsCredit Card ProcessingCryptography ExtensionsDatabase ExtensionsDate and Time Related ExtensionsFile System Related ExtensionsHuman Language and Character Encoding SupportImage Processing and GenerationMail Related ExtensionsMathematical ExtensionsNon-Text MIME OutputProcess Control ExtensionsOther Basic ExtensionsOther ServicesSearch Engine ExtensionsServer Specific ExtensionsSession ExtensionsText ProcessingVariable and Type Related ExtensionsWeb ServicesWindows Only ExtensionsXML ManipulationGUI ExtensionsKeyboard Shortcuts?This helpjNext menu itemkPrevious menu itemg pPrevious man pageg nNext man pageGScroll to bottomg gScroll to topg hGoto homepageg sGoto search(current page)/Focus search boxPHP is a popular general-purpose scripting language that is especially suited to web development.Fast, flexible and pragmatic, PHP powers everything from your blog to the most popular websites in the world.Download7.1.29·Release Notes·Upgrading7.2.18·Release Notes·Upgrading7.3.5·Release Notes·Upgrading03 May 2019PHP 7.1.29 ReleasedThe PHP development team announces the immediate availability of PHP
       7.1.29. This is a security release.All PHP 7.1 users are encouraged to upgrade to this version.For source downloads of PHP 7.1.29 please visit ourdownloads page,
       Windows source and binaries can be found onwindows.php.net/download/.
       The list of changes is recorded in theChangeLog.02 May 2019PHP 7.2.18 ReleasedThe PHP development team announces the immediate availability of PHP
     7.2.18. This is a security release which also contains several minor bug fixes.All PHP 7.2 users are encouraged to upgrade to this version.For source downloads of PHP 7.2.18 please visit ourdownloads page,
     Windows source and binaries can be found onwindows.php.net/download/.
     The list of changes is recorded in theChangeLog.02 May 2019PHP 7.3.5 Release AnnouncementThe PHP development team announces the immediate availability of PHP
      7.3.5. This is a security release which also contains several bug fixes.All PHP 7.3 users are encouraged to upgrade to this version.For source downloads of PHP 7.3.5 please visit ourdownloads page,
      Windows source and binaries can be found onwindows.php.net/download/.
      The list of changes is recorded in theChangeLog.04 Apr 2019PHP 7.1.28 ReleasedThe PHP development team announces the immediate availability of PHP
       7.1.28. This is a security release.All PHP 7.1 users are encouraged to upgrade to this version.For source downloads of PHP 7.1.28 please visit ourdownloads page,
       Windows source and binaries can be found onwindows.php.net/download/.
       The list of changes is recorded in theChangeLog.04 Apr 2019PHP 7.2.17 Release AnnouncementThe PHP development team announces the immediate availability of PHP 7.2.17.
     This is a security release which also contains several minor bug fixes.All PHP 7.2 users are encouraged to upgrade to this version.For source downloads of PHP 7.2.17 please visit ourdownloads page,
     Windows source and binaries can be found onwindows.php.net/download/.
     The list of changes is recorded in theChangeLog.04 Apr 2019PHP 7.3.4 Release AnnouncementThe PHP development team announces the immediate availability of PHP
       7.3.4. This is a security release which also contains several bug fixes.All PHP 7.3 users are encouraged to upgrade to this version.For source downloads of PHP 7.3.4 please visit ourdownloads page,
       Windows source and binaries can be found onwindows.php.net/download/.
       The list of changes is recorded in theChangeLog.22 Nov 2018PHP 7.3.0RC6 ReleasedThe PHP team is glad to announce the presumably last PHP 7.3.0 pre-release, PHP 7.3.0RC6.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0RC6 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be 7.3.0 (GA), planned for December 6th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.08 Nov 2018PHP 7.3.0RC5 ReleasedThe PHP team is glad to announce the next PHP 7.3.0 pre-release, PHP 7.3.0RC5.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0RC5 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be RC6, planned for November 22nd.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.25 Oct 2018PHP 7.3.0RC4 ReleasedThe PHP team is glad to announce the next PHP 7.3.0 pre-release, PHP 7.3.0RC4.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0RC4 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be RC5, planned for November 8th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.11 Oct 2018PHP 7.3.0RC3 ReleasedThe PHP team is glad to announce the next PHP 7.3.0 pre-release, PHP 7.3.0RC3.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0RC3 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be RC4, planned for October 25th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.28 Sep 2018PHP 7.3.0RC2 ReleasedThe PHP team is glad to announce the next PHP 7.3.0 pre-release, PHP 7.3.0RC2.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0RC2 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be RC3, planned for October 11th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.13 Sep 2018PHP 7.3.0RC1 ReleasedThe PHP team is glad to announce the release of the next PHP 7.3.0 pre-release, PHP 7.3.0RC1.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0RC1 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be RC2, planned for September 27th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.30 Aug 2018PHP 7.3.0.beta3 ReleasedThe PHP team is glad to announce the release of the seventh PHP 7.3.0 version, PHP 7.3.0beta3.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0beta3 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be RC1, planned for September 13th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.16 Aug 2018PHP 7.3.0.beta2 ReleasedThe PHP team is glad to announce the release of the sixth PHP 7.3.0 version, PHP 7.3.0beta2.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0beta2 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. Internal changes are listed in theUPGRADING.INTERNALSfile.
        These files can also be found in the release archive.The next release would be Beta 3, planned for August 30th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.02 Aug 2018PHP 7.3.0.beta1 ReleasedThe PHP team is glad to announce the release of the fifth PHP 7.3.0 version, PHP 7.3.0beta1.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0beta1 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.The next release would be Beta 2, planned for August 16th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.19 Jul 2018PHP 7.3.0alpha4 ReleasedThe PHP team is glad to announce the release of the fourth PHP 7.3.0 version, PHP 7.3.0alpha4.
        The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0alpha4 please visit thedownload page.
        Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
        or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.The next release would be Beta 1, planned for August 2nd.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.05 Jul 2018PHP 7.3.0 alpha 3 ReleasedThe PHP team is glad to announce the release of the third PHP 7.3.0 version, PHP 7.3.0 Alpha 3.
      The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0 Alpha 3 please visit thedownload page.
      Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
      or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.The next release would be Beta 1, planned for July 19th.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.21 Jun 2018PHP 7.3.0 alpha 2 ReleasedThe PHP team is glad to announce the release of the second PHP 7.3.0 version, PHP 7.3.0 Alpha 2.
      The rough outline of the PHP 7.3 release cycle is specified in thePHP Wiki.For source downloads of PHP 7.3.0 Alpha 2 please visit thedownload page.
      Windows sources and binaries can be found onwindows.php.net/qa/.Please carefully test this version and report any issues found in thebug reporting system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
      or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.The next release would be Alpha 3, planned for July 5.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.07 Jun 2018PHP 7.3.0 alpha 1 ReleasedPHP team is glad to announce the release of the first PHP 7.3.0 version, PHP 7.3.0 Alpha 1.
         This starts the PHP 7.3 release cycle, the rough outline of which is specified in thePHP Wiki.For source downloads of PHP 7.3.0 Alpha 1 please visit thedownload page.Please carefully test this version and report any issues found in thebug reporting system.Please DO NOT use this version in production, it is an early test version.For more information on the new features and other changes, you can read theNEWSfile,
             or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.The next release would be Alpha 2, planned for June 21.The signatures for the release can be found inthe manifestor onthe QA site.Thank you for helping us make PHP better.01 Feb 2018PHP 7.2.2 ReleasedThe PHP development team announces the immediate availability of PHP
      7.2.2. This is a bugfix release, with several bug fixes included.All PHP 7.2 users are encouraged to upgrade to this version.For source downloads of PHP 7.2.2 please visit ourdownloads page,
      Windows source and binaries can be found onwindows.php.net/download/.
      The list of changes is recorded in theChangeLog.12 Oct 2017PHP 7.2.0 Release Candidate 4 ReleasedThe PHP development team announces the immediate availability of PHP 7.2.0 RC4.
     This release is the fourth Release Candidate for 7.2.0.
     All users of PHP are encouraged to test this version carefully, and report any bugs
     and incompatibilities in thebug tracking system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
     or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.For source downloads of PHP 7.2.0 Release Candidate 4 please visit thedownloadpage,
     Windows sources and binaries can be found atwindows.php.net/qa/.The next Release Candidate will be announced on the 26th of October.
     You can also read the full list of planned releases onour wiki.Thank you for helping us make PHP better.28 Sep 2017PHP 7.2.0 Release Candidate 3 ReleasedThe PHP development team announces the immediate availability of PHP 7.2.0 RC3.
     This release is the third Release Candidate for 7.2.0.
     All users of PHP are encouraged to test this version carefully, and report any bugs
     and incompatibilities in thebug tracking system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
     or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.For source downloads of PHP 7.2.0 Release Candidate 3 please visit thedownloadpage,
     Windows sources and binaries can be found atwindows.php.net/qa/.The next Release Candidate will be announced on the 12th of October.
     You can also read the full list of planned releases onour wiki.Thank you for helping us make PHP better.31 Aug 2017PHP 7.2.0 Release Candidate 1 ReleasedThe PHP development team announces the immediate availability of PHP 7.2.0 Release
      Candidate 1. This release is the first Release Candidate for 7.2.0.
      All users of PHP are encouraged to test this version carefully, and report any bugs
      and incompatibilities in thebug tracking system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
      or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.For source downloads of PHP 7.2.0 Release Candidate 1 please visit thedownloadpage,
      Windows sources and binaries can be found atwindows.php.net/qa/.The second Release Candidate will be released on the 14th of September.
      You can also read the full list of planned releases onour wiki.Thank you for helping us make PHP better.17 Aug 2017PHP 7.2.0 Beta 3 ReleasedThe PHP development team announces the immediate availability of PHP 7.2.0 Beta 3.
      This release is the third and final beta for 7.2.0. All users of PHP are encouraged
      to test this version carefully, and report any bugs and incompatibilities in thebug tracking system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For more information on the new features and other changes, you can read theNEWSfile,
      or theUPGRADINGfile for a complete list of upgrading notes. These files can also be found in the release archive.For source downloads of PHP 7.2.0 Beta 3 please visit thedownloadpage,
      Windows sources and binaries can be found atwindows.php.net/qa/.The first Release Candidate will be released on the 31th of August.
      You can also read the full list of planned releases onour wiki.Thank you for helping us make PHP better.06 Jul 2017PHP 7.2.0 Alpha 3 ReleasedThe PHP development team announces the immediate availability of PHP 7.2.0 Alpha 3.
     This release contains fixes and improvements relative to Alpha 2.
     All users of PHP are encouraged to test this version carefully,
     and report any bugs and incompatibilities in thebug tracking system.THIS IS A DEVELOPMENT PREVIEW - DO NOT USE IT IN PRODUCTION!For information on new features and other changes, you can read theNEWSfile,
     or theUPGRADINGfile
     for a complete list of upgrading notes. These files can also be found in the release archive.For source downloads of PHP 7.2.0 Alpha 3 please visit thedownloadpage,
     Windows sources and binaries can be found onwindows.php.net/qa/.The first beta will be released on the 20th of July. You can also read the full list of planned releases on ourwiki.Thank you for helping us make PHP better.Older News EntriesConferences calling for papersphp[world] 2019Upcoming conferencesCoderCruise 2019PHPConf.Asia 2019SymfonyCon Amsterdam 2019SymfonyLive Berlin 2019User Group EventsSpecial ThanksSocial media@official_phpCopyright © 2001-2019 The PHP GroupMy PHP.netContactOther PHP.net sitesPrivacy policy
"""
tokens=[t for t in text.split()]
#print (tokens)

import nltk
freq=nltk.FreqDist(tokens)
for key,val in freq.items():
    print ((key)+str(val))