#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-exec-maven-plugin
Version  : 1.6.0
Release  : 2
URL      : https://github.com/mojohaus/exec-maven-plugin/archive/exec-maven-plugin-1.6.0.tar.gz
Source0  : https://github.com/mojohaus/exec-maven-plugin/archive/exec-maven-plugin-1.6.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/codehaus/mojo/exec-maven-plugin/1.6.0/exec-maven-plugin-1.6.0.jar
Source2  : https://repo.maven.apache.org/maven2/org/codehaus/mojo/exec-maven-plugin/1.6.0/exec-maven-plugin-1.6.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-exec-maven-plugin-data = %{version}-%{release}

%description
# MojoHaus Exec Maven Plugin
This is the [exec-maven-plugin](http://www.mojohaus.org/exec-maven-plugin/).
[![Apache License, Version 2.0, January 2004](https://img.shields.io/github/license/mojohaus/sql-maven-plugin.svg?label=License)](http://www.apache.org/licenses/)
[![Maven Central](https://img.shields.io/maven-central/v/org.codehaus.mojo/exec-maven-plugin.svg?label=Maven%20Central)](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.codehaus.mojo%22%20a%3A%22exec-maven-plugin%22)
[![Build Status](https://travis-ci.org/mojohaus/exec-maven-plugin.svg?branch=master)](https://travis-ci.org/mojohaus/exec-maven-plugin)
[![Build Status (AppVeyor)](https://ci.appveyor.com/api/projects/status/github/mojohaus/exec-maven-plugin?branch=master&svg=true)](https://ci.appveyor.com/project/khmarbaise/exec-maven-plugin)

%package data
Summary: data components for the mvn-exec-maven-plugin package.
Group: Data

%description data
data components for the mvn-exec-maven-plugin package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/exec-maven-plugin/1.6.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/exec-maven-plugin/1.6.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/exec-maven-plugin/1.6.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/exec-maven-plugin/1.6.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/mojo/exec-maven-plugin/1.6.0/exec-maven-plugin-1.6.0.jar
/usr/share/java/.m2/repository/org/codehaus/mojo/exec-maven-plugin/1.6.0/exec-maven-plugin-1.6.0.pom
