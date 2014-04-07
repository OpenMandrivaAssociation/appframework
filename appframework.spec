%{?_javapackages_macros:%_javapackages_macros}
%if 0%{?fedora}
%else
%define __cp /bin/cp
%endif
Name:    appframework
Version: 1.03
Release: 12.0%{?dist}
Summary: Swing Application Framework
License: LGPLv2+
URL:     https://appframework.dev.java.net/
Group:   Development/Libraries

Source0: https://appframework.dev.java.net/downloads/AppFramework-1.03-src.zip
Patch0:  %{name}-%{version}-no-local-storage.diff
Patch1:  %{name}-%{version}-openjdk.diff

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: swing-layout >= 1.0.3

Requires: java >= 1:1.6.0
Requires: jpackage-utils

Requires: swing-layout >= 1.0.3

BuildArch: noarch

%description
The JSR-296 Swing Application Framework prototype implementation is a small 
set of Java classes that simplify building desktop applications.

%package javadoc
Summary: Javadoc for %{name}
Group:   Documentation

%description javadoc
Javadoc for %{name}.

%prep

%setup -q -n AppFramework-%{version}

# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%patch0
%patch1 -p1

%build
%{ant} -Dlibs.swing-layout.classpath=%{_javadir}/swing-layout.jar dist

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/AppFramework-1.03.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(-,root,root,-)
%{_javadir}/*
%doc COPYING README

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

%changelog
* Mon Aug 05 2013 Omair Majid <omajid@redhat.com> - 1.03-12
- Update to comply with latest guidelines
- Fix build dependencies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 27 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.03-4
- The %%defattr(-,root,root,-) is used everywhere

* Mon Aug 25 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.03-3
- Use the %%{ant} instead of the ant command
- Use the %%{version} in the "-n" option of the %%setup

* Wed Aug 14 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.03-2
- java-devel & jpackage-utils are added as the build requirements.
- jpackage-utils is added as the run-time requirement.
- Appropriate values of Group Tags are chosen from the official list.
- Redundant run-time requirements for /bin/* utilities are removed.
- A ghost symlink for javadoc package is removed.
- Documentation added.
- Both build-time and run-time requirements for the swing-layout package are added.
- Redundant dependency on swing-worker is removed.

* Mon Jul 14 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.03-1
- Fix version number 1.0.3 -> 1.03 .
- Remove swingworker from requirement due to JRE 6 includes it.
- Fix Summary.
- Change BuldRoot.
- Bootstrap into Fedora.

* Thu Jun 19 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.0.3-3mdv2009.0
+ Revision: 226162
- rebuild

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:1.0.3-2mdv2008.1
+ Revision: 120823
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Thu Dec 13 2007 Jaroslav Tulach <jtulach@mandriva.org> 0:1.0.3-1mdv2008.1
+ Revision: 119282
- Removing support for JNLP mode, as the classes needed for compilation do not seem to be present in Iced Tea
- Initial package for Swing Application Framework
- create appframework
