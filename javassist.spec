%{?scl:%scl_package javassist}
%{!?scl:%global pkg_name %{name}}

%{?thermostat_find_provides_and_requires}

Name:           %{?scl_prefix}javassist
Version:        3.16.1
Release:        9.1%{?dist}
Summary:        The Java Programming Assistant provides simple Java bytecode manipulation
Group:          Development/Libraries
License:        MPLv1.1 or LGPLv2+ or ASL 2.0
URL:            http://www.csg.is.titech.ac.jp/~chiba/javassist/
Source0:        http://downloads.sourceforge.net/jboss/%{pkg_name}-%{version}-GA.zip
BuildArch:      noarch

BuildRequires:     java7-devel
BuildRequires:     jpackage-utils

BuildRequires:     maven-local
BuildRequires:     maven-compiler-plugin
BuildRequires:     maven-install-plugin
BuildRequires:     maven-jar-plugin
BuildRequires:     maven-javadoc-plugin
BuildRequires:     maven-resources-plugin
BuildRequires:     maven-surefire-plugin
BuildRequires:     maven-surefire-provider-junit
BuildRequires:     maven-source-plugin
BuildRequires:     maven-antrun-plugin
BuildRequires:     maven-doxia-sitetools

%description
Javassist enables Java programs to define a new class at runtime and to
modify a class file when the JVM loads it. Unlike other similar
bytecode editors, Javassist provides two levels of API: source level
and bytecode level. If the users use the source-level API, they can
edit a class file without knowledge of the specifications of the Java
bytecode. The whole API is designed with only the vocabulary of the
Java language. You can even specify inserted bytecode in the form of
source text; Javassist compiles it on the fly. On the other hand, the
bytecode-level API allows the users to directly edit a class file as
other editors.

%package javadoc
Summary:           Javadocs for javassist
Group:             Documentation

%description javadoc
javassist development documentation.

%prep
%{?scl:scl enable %{scl} - << "EOF"}
%setup -q -n %{pkg_name}-%{version}-GA

mkdir runtest
find . -name \*.jar -type f -delete

%mvn_file : %{pkg_name}
%mvn_alias : "%{pkg_name}:%{pkg_name}"

%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc License.html Readme.html

%files javadoc -f .mfiles-javadoc
%doc License.html

%changelog
* Tue Jan 21 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.16.1-9.1
- Rebuild to fix provides/requires

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.16.1-9
- Remove system-scoped dependency on tools.jar

* Tue Nov 12 2013 Michal Srb <msrb@redhat.com> - 3.16.1-8.1
- Enable SCL for thermostat

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 3.16.1-8
- Migrate away from mvn-rpmbuild (Resolves: #997484)

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.16.1-7
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.16.1-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Feb 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.16.1-5
- Remove unneeded BR on maven-doxia
- Resolves: rhbz#915607

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.16.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Andy Grimm <agrimm@gmail.com> - 3.16.1-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Alexander Kurtakov <akurtako@redhat.com> 3.15.0-1
- Update to latest upstream release.
- Add javassist:javassist depmap.
- The project is now triple licensed.

* Wed Aug 31 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.14.0-5
- Fixes according to current guidelines

* Tue Aug 30 2011 Andy Grimm <agrimm@gmail.com> - 3.14.0-4
- Switch to Maven 3 build.

* Tue Aug 30 2011 John5342 <john5342 at, fedoraproject.org> - 3.14.0-3
- Remove ext_ver macro usage leftover after last rebase (rhbz#734255)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 4 2010 Alexander Kurtakov <akurtako@redhat.com> 3.14.0-1
- Update to 3.14.0 upstream version.
- Various fixes in preparation for merge review.

* Fri Feb 12 2010 Alexander Kurtakov <akurtako@redhat.com> 3.9.0-7
- Add maven-doxia BRs.

* Fri Feb 12 2010 Alexander Kurtakov <akurtako@redhat.com> 3.9.0-6
- Remove not needed BR. Fixes rhbz#539176.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 John5342 <john5342 at, fedoraproject.org> - 3.9.0-3
- Correct group id for maven depmap

* Mon Jan 26 2009 John5342 <john5342 at, fedoraproject.org> - 3.9.0-2
- Build using maven and install maven stuff (fixes bug 480428)

* Tue Dec 16 2008 Sandro Mathys <red at fedoraproject.org> - 3.9.0-1
- initial build
