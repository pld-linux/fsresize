%define ver     0.08
%define release 1

Summary: FAT16 and FAT32 resizer for Linux
Name: fsresize
Version: %ver
Release: %release
Copyright: GPL
Group: Utilities/System
Source: http://www.alphalink.com.au/~clausen/fsresize/fsresize-%{ver}.tar.gz
BuildRoot: /tmp/fsresize-root
Packager: Andrew Clausen <clausen@alphalink.com.au>
URL: http://www.alphalink.com.au/~clausen/fsresize

%description
FAT16 and FAT32 resizer for Linux.

%changelog

%prep
%setup

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}
install -m755 fsresize      $RPM_BUILD_ROOT/usr/sbin/fsresize
install -m444 fsresize.8    $RPM_BUILD_ROOT/usr/man/man8/fsresize.8

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc README HACKING TODO
%attr(-, root, root)    /usr/sbin/fsresize
%attr(-, root, root)    /usr/man/man8/fsresize.8
