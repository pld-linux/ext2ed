Summary:	ext2 filesystem editor for hackers *only*
Summary(de):	ext2-Dateisystem-Editor NUR für Hacker  
Summary(fr):	éditeur du système de fichiers ext2, *uniquement* pour les hackers
Summary(pl):	Edytor systemu plików ext2 - TYLKO DLA DO¦WIADCZONYCH U¯YTKOWNIKÓW
Summary(tr):	ext2 dosya sistemi düzenleyicisi
Name:		ext2ed
Version:	0.1
Release:	16
Copyright:	GPL
Group:		Utilities/System
Source:		ftp://sunsite.unc.edu/pub/Linux/system/filesystems/ext2/%{name}-%{version}.tar.gz
Patch:		ext2ed-config.patch
Patch1:		ext2ed-inode.patch
Patch2:		ext2ed-glibc.patch
Patch3:		ext2ed-opt.patch
Patch4:		ext2ed-FHS2.0.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch4 -p1

%build
rm -f ext2ed
make 
strip ext2ed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man8,var/state/ext2ed}

make install \
	VAR_DIR=$RPM_BUILD_ROOT/var/state/ext2ed \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	DOC_DIR=$RPM_BUILD_ROOT \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* README doc/*.ps

%files
%defattr(644,root,root,755)
%doc README.gz doc/*.sgml doc/*.ps.gz
%attr(700,root,root) %dir /var/state/ext2ed
%attr(600,root,root) %config /var/state/ext2ed/*
%attr(700,root,root) %{_bindir}/ext2ed
%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT
