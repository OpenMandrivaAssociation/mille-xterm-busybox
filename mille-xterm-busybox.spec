Summary:	Multi-call binary combining many common Unix tools into one executable
Name:		mille-xterm-busybox
Version:	1.1.2
Release:	%mkrel 7
License:	GPL
Group:		Shells
URL:		http://www.busybox.net/
Source0:	http://www.busybox.net/downloads/busybox-%{version}.tar.bz2
Source1:	http://www.busybox.net/downloads/busybox-%{version}.tar.bz2.sign
Source2:	busybox-%{version}.config
Patch0:		udhcp-altport.diff
Patch1:		udhcp-rootpath.diff
BuildRequires:	gcc >= 3.3.1-2mdk
BuildRequires:	uClibc-static-devel >= 0.9.26-5mdk
Conflicts:	busybox
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the utilities
you usually find in GNU coreutils, shellutils, etc. The utilities in BusyBox
generally have fewer options than their full-featured GNU cousins; however, the
options that are included provide the expected functionality and behave very
much like their GNU counterparts. BusyBox provides a fairly complete POSIX
environment for any small or embedded system.

BusyBox has been written with size-optimization and limited resources in mind.
It is also extremely modular so you can easily include or exclude commands (or
features) at compile time. This makes it easy to customize your embedded
systems. To create a working system, just add /dev, /etc, and a kernel.

%prep

%setup -q -n busybox-%{version}
%patch0 -p1
%patch1 -p1
cp %{SOURCE2} .config
perl -pi -e "s#-march=i386#-march=i586 -mtune=pentiumpro#g" Rules.mak

%build
make oldconfig
make dep
uclibc make

%install
rm -rf %{buildroot}

install -d %{buildroot}/bin
install -d %{buildroot}%{_mandir}/man1/busybox.1

install -m0755 busybox %{buildroot}/bin/busybox
install -m0644 docs/BusyBox.1 %{buildroot}%{_mandir}/man1/busybox.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL README TODO docs/BusyBox.txt
/bin/busybox
%{_mandir}/man1/busybox.1*


