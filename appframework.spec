Name:    appframework
Version: 1.03
Release: 8
Summary: Swing Application Framework
License: LGPLv2+
URL:     https://appframework.dev.java.net/
Group:   Development/Java 

Source0: https://appframework.dev.java.net/downloads/AppFramework-1.03-src.zip
Patch0:  %{name}-%{version}-no-local-storage.diff
Patch1:  %{name}-%{version}-openjdk.diff

BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: java-devel >= 0:1.6.0
BuildRequires: jpackage-utils
BuildRequires: swing-layout >= 1.0.3

Requires: java >= 0:1.6.0
Requires: jpackage-utils
Requires: swing-layout >= 1.0.3

BuildArch: noarch

%description
The JSR-296 Swing Application Framework prototype implementation is a small 
set of Java classes that simplify building desktop applications.

%package javadoc
Summary: Javadoc for %{name}
Group:   Development/Java

%description javadoc
Javadoc for %{name}.

%prep

%setup -q -n AppFramework-%{version}

# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%patch0 -p0 -b .sav
%patch1 -p1 -b .sav

%build
%{ant} -Dlibs.swing-layout.classpath=%{_javadir}/swing-layout.jar dist

%install
%{__rm} -fr %{buildroot}
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/AppFramework-1.03.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_javadir}/*
%doc COPYING README

%files javadoc
%defattr(-,root,root,-)
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*

