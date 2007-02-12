Summary:	FAT16 and FAT32 resizer for Linux
Summary(pl.UTF-8):   Program do zmiany rozmiaru partycji FAT16 i FAT32
Name:		fsresize
Version:	0.08
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.alphalink.com.au/~clausen/fsresize/%{name}-%{version}.tar.gz
# Source0-md5:	4c1b3336aef88a8f2b370d3f164e6051
URL:		http://www.alphalink.com.au/~clausen/fsresize/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAT16 and FAT32 resizes your FAT16 and FAT32 partitions. There is no
need to defragment (this'll do it for you!) It's running quite
acceptably speed-wise.

%description -l pl.UTF-8
Program ten służy do zmiany rozmiaru partycji FAT16 i FAT32. Nie
trzeba ich wcześniej defragmentować (program sam zatroszczy się o co
trzeba!). Szybkość programu jest zadowalająca.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install fsresize $RPM_BUILD_ROOT%{_sbindir}
install fsresize.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HACKING TODO
%attr(755,root,root) %{_sbindir}/fsresize
%{_mandir}/man8/*
