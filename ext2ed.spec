Summary:     ext2 filesystem editor for hackers *only*
Summary(de): ext2-Dateisystem-Editor NUR für Hacker  
Summary(fr): éditeur du système de fichiers ext2, *uniquement* pour les hackers
Summary(pl): Edytor systemu plików ext2 - TYLKO DLA DO¦WIADCZONYCH U¯YTKOWNIKÓW
Summary(tr): ext2 dosya sistemi düzenleyicisi
Name:        ext2ed
Version:     0.1
Release:     16
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://sunsite.unc.edu/pub/Linux/system/filesystems/ext2/%{name}-%{version}.tar.gz
Patch:       ext2ed-config.patch
Patch1:      ext2ed-inode.patch
Patch2:      ext2ed-glibc.patch
Patch3:      ext2ed-opt.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a package to allow for hacking of your extended two file systems. It
is for hackers *only* and should only be used by experienced personnel. If
you aren't sure if this is you, it isn't. Also, do not smoke near this
software. You have been warned. This is not a recording.

%description -l de
Dies ist ein Paket zum Hacken der ext2-Dateisysteme, zum AUSSCHLIESSLICHEN
Gebrauch durch Hacker und versierte Fachleute.  Wenn Sie sich nicht
angesprochen fühlen, lassen Sie lieber die Hände davon! Und noch etwas:
Zünden Sie sich in der Nähe dieser Software keine Zigarette an - sagen Sie
nicht, wir hätten Sie nicht gewarnt.

%description -l fr
Paquetage permettant le hackind des systèmes de fichiers ext2. Il n'est
*que* pour les hackers et doit être utilisés par des gens expérimentés. Si
vous n'êtes pas sûr de l'être, vous ne l'êtes pas. Ne fumez pas près de ce
logiciel. Vous aurez été prévenu, ce n'est pas un exercice.

%description -l pl
Ext2ed pozwala na modyfikowanie systemu plików ext2. Przeznaczony jest tylko
i wy³±cznie dla do¶wiadczonych u¿ytkowników Linuxa. Niedo¶wiadczeni oraz
¶rednio-zaawansowani u¿ytkownicy nie powinni siê nawet zbli¿aæ do ext2ed.

W pobli¿u ext2ed obowi±zuje ca³kowity zakaz palenia tytoniu ;)

%description -l tr
Bu yazýlýmlarla ext2 dosya sistemi üzerinde deðiþiklikler yapabilirsiniz. Bu
yazýlýmý sadece ne yaptýðýnýzdan kesinkle eminseniz kullanýn. Dosyalarýnýzý
kaybedecek olursanýz, unutmayýn: sizi uyarmýþtýk!

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f ext2ed
make 
strip ext2ed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/{bin,man/man8},var/lib/ext2ed}

make install \
	VAR_DIR=$RPM_BUILD_ROOT/var/lib/ext2ed \
	BIN_DIR=$RPM_BUILD_ROOT/usr/bin \
	DOC_DIR=$RPM_BUILD_ROOT \
	MAN_DIR=$RPM_BUILD_ROOT/usr/man/man8

gzip -9nf $RPM_BUILD_ROOT/usr/man/man8/*

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
* Mon Dec 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1-16]
- added gzipping man pages.

* Mon Oct 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1-15]
- added using $PRPM_OPT_FLAGS during compile (ext2ed-opt.patch).

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
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
