Summary:	FAT16 and FAT32 resizer for Linux
Name:		fsresize
Version:	0.08
Release:	2
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		http://www.alphalink.com.au/~clausen/fsresize/%{name}-%{version}.tar.gz
URL:		http://www.alphalink.com.au/~clausen/fsresize/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
FAT16 and FAT32 resizes your FAT16 and FAT32 partitions. There is no need to
defragment (this'll do it for you!) It's running quite acceptably
speed-wise.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install -s fsresize $RPM_BUILD_ROOT%{_sbindir}
install fsresize.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README HACKING TODO
%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root)  /usr/sbin/fsresize
%{_mandir}/man8/*
