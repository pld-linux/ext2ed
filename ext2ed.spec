Summary:	ext2 filesystem editor for hackers *only*
Summary(de):	ext2-Dateisystem-Editor NUR f�r Hacker
Summary(fr):	�diteur du syst�me de fichiers ext2, *uniquement* pour les hackers
Summary(pl):	Edytor systemu plik�w ext2 - TYLKO DLA DO�WIADCZONYCH U�YTKOWNIK�W
Summary(tr):	ext2 dosya sistemi d�zenleyicisi
Name:		ext2ed
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/filesystems/ext2/%{name}-%{version}.tar.gz
# Source0-md5:	996bbbecceee1eb95e4cdbc53a1860df
Patch0:		%{name}-opt.patch
Patch1:		%{name}-FHS2.0.patch
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package to allow for hacking of your extended two file
systems. It is for hackers *only* and should only be used by
experienced personnel. If you aren't sure if this is you, it isn't.
Also, do not smoke near this software. You have been warned. This is
not a recording.

%description -l de
Dies ist ein Paket zum Hacken der ext2-Dateisysteme, zum
AUSSCHLIESSLICHEN Gebrauch durch Hacker und versierte Fachleute. Wenn
Sie sich nicht angesprochen f�hlen, lassen Sie lieber die H�nde davon!
Und noch etwas: Z�nden Sie sich in der N�he dieser Software keine
Zigarette an - sagen Sie nicht, wir h�tten Sie nicht gewarnt.

%description -l fr
Paquetage permettant le hackind des syst�mes de fichiers ext2. Il
n'est *que* pour les hackers et doit �tre utilis�s par des gens
exp�riment�s. Si vous n'�tes pas s�r de l'�tre, vous ne l'�tes pas. Ne
fumez pas pr�s de ce logiciel. Vous aurez �t� pr�venu, ce n'est pas un
exercice.

%description -l pl
Ext2ed pozwala na modyfikowanie systemu plik�w ext2. Przeznaczony jest
tylko i wy��cznie dla do�wiadczonych u�ytkownik�w Linuksa.
Niedo�wiadczeni oraz �rednio-zaawansowani u�ytkownicy nie powinni si�
nawet zbli�a� do ext2ed.

W pobli�u ext2ed obowi�zuje ca�kowity zakaz palenia tytoniu ;)

%description -l tr
Bu yaz�l�mlarla ext2 dosya sistemi �zerinde de�i�iklikler
yapabilirsiniz. Bu yaz�l�m� sadece ne yapt���n�zdan kesinkle eminseniz
kullan�n. Dosyalar�n�z� kaybedecek olursan�z, unutmay�n: sizi
uyarm��t�k!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f ext2ed
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man8,var/lib/ext2ed}

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
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /var/lib/ext2ed/ext2ed.conf
%attr(744,root,root) %{_bindir}/ext2ed
%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT
