Summary:     ext2 filesystem editor for hackers *only*
Summary(de): ext2-Dateisystem-Editor NUR f�r Hacker  
Summary(fr): �diteur du syst�me de fichiers ext2, *uniquement* pour les hackers
Summary(pl): Edytor systemu plik�w ext2 - TYLKO DLA DO�WIADCZONYCH U�YTKOWNIK�W
Summary(tr): ext2 dosya sistemi d�zenleyicisi
Name:        ext2ed
Version:     0.1
Release:     15
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://sunsite.unc.edu/pub/Linux/system/filesystems/ext2/%{name}-%{version}.tar.gz
Patch:       ext2ed-0.1-config.patch
Patch1:      ext2ed-0.1-inode.patch
Patch2:      ext2ed-0.1-glibc.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a package to allow for hacking of your extended two file
systems.  It is for hackers *only* and should only be used by
experienced personnel.  If you aren't sure if this is you, it
isn't.  Also, do not smoke near this software.  You have been
warned.  This is not a recording.

%description -l de
Dies ist ein Paket zum Hacken der ext2-Dateisysteme, zum 
AUSSCHLIESSLICHEN Gebrauch durch Hacker und versierte Fachleute. 
Wenn Sie sich nicht angesprochen f�hlen, lassen Sie lieber die 
H�nde davon! Und noch etwas: Z�nden Sie sich in der N�he dieser 
Software keine Zigarette an - sagen Sie nicht, wir h�tten Sie 
nicht gewarnt. 

%description -l fr
Paquetage permettant le hackind des syst�mes de fichiers ext2.
Il n'est *que* pour les hackers et doit �tre utilis�s par des
gens exp�riment�s. Si vous n'�tes pas s�r de l'�tre, vous ne
l'�tes pas. Ne fumez pas pr�s de ce logiciel. Vous aurez �t�
pr�venu, ce n'est pas un exercice.

%description -l pl
Ext2ed pozwala na modyfikowanie systemu plik�w ext2. Przeznaczony jest tylko i
wy��cznie dla do�wiadczonych u�ytkownik�w Linuxa. Niedo�wiadczeni oraz 
�rednio-zaawansowani u�ytkownicy nie powinni si� nawet zbli�a� do ext2ed. 

    W pobli�u ext2ed obowi�zuje ca�kowity zakaz palenia tytoniu ;)

%description -l tr
Bu yaz�l�mlarla ext2 dosya sistemi �zerinde de�i�iklikler yapabilirsiniz.
Bu yaz�l�m� sadece ne yapt���n�zdan kesinkle eminseniz kullan�n.
Dosyalar�n�z� kaybedecek olursan�z, unutmay�n: sizi uyarm��t�k!

%prep
%setup -q
%patch -p0 -b .config
%patch1 -p1 -b .inode
%patch2 -p1 -b .glibc

%build
rm -f ext2ed
make 
strip ext2ed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/{bin,man/man8},var/lib/ext2ed}

make 	VAR_DIR=$RPM_BUILD_ROOT/var/lib/ext2ed \
	BIN_DIR=$RPM_BUILD_ROOT/usr/bin \
	DOC_DIR=$RPM_BUILD_ROOT \
	MAN_DIR=$RPM_BUILD_ROOT/usr/man/man8 \
	install 

%files
%defattr(644,root,root,755)
%doc README doc/*.sgml doc/*.ps
%attr(700, root, root) %dir /var/lib/ext2ed
%attr(600, root, root) %config /var/lib/ext2ed/*
%attr(700, root, root) /usr/bin/ext2ed
%attr(644, root,  man) /usr/man/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Oct 06 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [0.1-15]
- added pl translation,
- added Buildroot support,
- restricted files permissions,
- build from non root's account,
- major modifications of the spec file.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses
- updated bad patch (!)

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- various spec file clean ups

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- build against readline library w/ proper soname

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
