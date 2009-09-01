%define section		free

Name:		appframework
Version:	1.0.3
Release:	%mkrel 4
Epoch:		0
Summary:        Swing Application Framework API
License:        LGPL
Url:            https://appframework.dev.java.net/
Group:		Development/Java
#
Source0:        https://appframework.dev.java.net/downloads/AppFramework-1.03-src.zip
Patch0:         no-local-storage.diff
BuildRequires:	java-rpmbuild >= 1.6
BuildRequires:	java >= 1.6
BuildRequires:	java-devel >= 1.6
BuildRequires:	swingworker >= 1.2.1
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
Requires:	swingworker >= 1.2.1
Requires:	java >= 1.6
BuildArch:      noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The JSR-296 Swing Application Framework prototype implementation is a small 
set of Java classes that simplify building desktop applications.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires(post):   /bin/rm,/bin/ln
Requires(postun): /bin/rm

%description javadoc
Javadoc for %{name}.

%prep
%{__rm} -fr %{buildroot}
%setup -q -n AppFramework-1.03
# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%patch0

%{__ln_s} %{_javadir}/swingworker.jar lib/swing-worker.jar

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
ant dist -verbose

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/AppFramework-1.03.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%clean
%{__rm} -rf %{buildroot}

%post javadoc
%{__rm} -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ $1 -eq 0 ]; then
  %{__rm} -f %{_javadocdir}/%{name}
fi

%files
%defattr(-,root,root)
%{_javadir}/*


%files javadoc
%defattr(-,root,root)
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%ghost %{_javadocdir}/%{name}
