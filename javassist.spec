%{?scl:%scl_package javassist}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global upstream_version rel_%(sed s/\\\\./_/g <<<"%{version}")_ga

Name:           %{?scl_prefix}javassist
Version:        3.18.1
Release:        4.1%{?dist}
Summary:        The Java Programming Assistant provides simple Java bytecode manipulation
Group:          Development/Libraries
License:        MPLv1.1 or LGPLv2+ or ASL 2.0
URL:            http://www.csg.is.titech.ac.jp/~chiba/%{pkg_name}/
BuildArch:      noarch

Source0:        http://github.com/jboss-%{pkg_name}/%{pkg_name}/archive/%{upstream_version}.tar.gz

Patch0:         0001-Remove-usage-of-junit.awtui-and-junit.swingui.patch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}mvn(junit:junit)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-source-plugin)

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
Requires:          %{?scl_prefix_java_common}jpackage-utils

%description javadoc
javassist development documentation.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n %{pkg_name}-%{upstream_version}
find . -name \*.jar -type f -delete
mkdir runtest
%patch0 -p1
%pom_xpath_remove "pom:profile[pom:id='default-tools']"
%pom_add_dep com.sun:tools

%mvn_file : %{pkg_name}
%mvn_alias : %{pkg_name}:%{pkg_name}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# TODO: enable tests
%mvn_build -f
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc License.html Readme.html

%files javadoc -f .mfiles-javadoc
%doc License.html

%changelog
* Tue Jul 07 2015 Mat Booth <mat.booth@redhat.com> - 3.18.1-4.1
- Import latest from Fedora

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.18.1-3
- Simplify build dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.18.1-1
- Update to upstream version 3.18.1
- Remove workaround for rpm bug, can be removed in F-18
- Update to current packaging guidelines

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.16.1-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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