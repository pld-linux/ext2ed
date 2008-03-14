Summary:	ext2 filesystem editor for hackers *only*
Summary(de.UTF-8):	ext2-Dateisystem-Editor NUR für Hacker
Summary(fr.UTF-8):	éditeur du système de fichiers ext2, *uniquement* pour les hackers
Summary(pl.UTF-8):	Edytor systemu plików ext2 - TYLKO DLA DOŚWIADCZONYCH UŻYTKOWNIKÓW
Summary(tr.UTF-8):	ext2 dosya sistemi düzenleyicisi
Name:		ext2ed
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/filesystems/ext2/%{name}-%{version}.tar.gz
# Source0-md5:	996bbbecceee1eb95e4cdbc53a1860df
Patch0:		%{name}-opt.patch
Patch1:		%{name}-FHS2.0.patch
Patch2:		%{name}-nooldext2acl.patch
Patch3:		%{name}-header.patch
BuildRequires:	e2fsprogs-devel
BuildRequires:	readline-devel >= 4.2
# according to comments in e2fsprogs, ext2ed code assumes that CPU
# is 32-bit little endian - on other platforms it can only break something
# (another thing is that it doesn't support >2GB filesystems at all)
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package to allow for hacking of your extended two file
systems. It is for hackers *only* and should only be used by
experienced personnel. If you aren't sure if this is you, it isn't.
Also, do not smoke near this software. You have been warned. This is
not a recording.

%description -l de.UTF-8
Dies ist ein Paket zum Hacken der ext2-Dateisysteme, zum
AUSSCHLIESSLICHEN Gebrauch durch Hacker und versierte Fachleute. Wenn
Sie sich nicht angesprochen fühlen, lassen Sie lieber die Hände davon!
Und noch etwas: Zünden Sie sich in der Nähe dieser Software keine
Zigarette an - sagen Sie nicht, wir hätten Sie nicht gewarnt.

%description -l fr.UTF-8
Paquetage permettant le hackind des systèmes de fichiers ext2. Il
n'est *que* pour les hackers et doit être utilisés par des gens
expérimentés. Si vous n'êtes pas sûr de l'être, vous ne l'êtes pas. Ne
fumez pas près de ce logiciel. Vous aurez été prévenu, ce n'est pas un
exercice.

%description -l pl.UTF-8
Ext2ed pozwala na modyfikowanie systemu plików ext2. Przeznaczony jest
tylko i wyłącznie dla doświadczonych użytkowników Linuksa.
Niedoświadczeni oraz średnio-zaawansowani użytkownicy nie powinni się
nawet zbliżać do ext2ed.

W pobliżu ext2ed obowiązuje całkowity zakaz palenia tytoniu ;)

%description -l tr.UTF-8
Bu yazılımlarla ext2 dosya sistemi üzerinde değişiklikler
yapabilirsiniz. Bu yazılımı sadece ne yaptığınızdan kesinkle eminseniz
kullanın. Dosyalarınızı kaybedecek olursanız, unutmayın: sizi
uyarmıştık!

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f ext2ed
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,/var/lib/ext2ed}

%{__make} install \
	VAR_DIR=$RPM_BUILD_ROOT/var/lib/ext2ed \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	DOC_DIR=$RPM_BUILD_ROOT \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man8

%files
%defattr(644,root,root,755)
%doc README doc/*.sgml doc/*.ps
%attr(750,root,root) %dir /var/lib/ext2ed
/var/lib/ext2ed/ext2.descriptors
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /var/lib/ext2ed/ext2ed.conf
%attr(744,root,root) %{_bindir}/ext2ed
%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT
