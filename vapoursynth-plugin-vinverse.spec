Summary:	Vapoursynth filter to remove (residual) combing
Summary(pl.UTF-8):	Filtr Vapoursynth do usuwania (resztkowego) efektu grzebienia
Name:		vapoursynth-plugin-vinverse
# 44-4 was last version of vapoursynth package containing plugin
Version:	44
Release:	5
License:	GPL v2+
Group:		Libraries
%define	gitref	acdeca22038583d73d420ccf76d0658f06cae3c0
Source0:	https://github.com/vapoursynth/vs-vinverse-obsolete/archive/%{gitref}/vs-vinverse-obsolete-%{gitref}.tar.gz
# Source0-md5:	8cb5fa385e9d8743945bf3be5c413ed8
URL:		https://github.com/vapoursynth/vs-vinverse-obsolete
BuildRequires:	libtool >= 2:1.5
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vinverse is a simple filter to remove (residual) combing, based on an
AviSynth script by Didee
<http://forum.doom9.org/showthread.php?p=841641#post841641>.

%description -l pl.UTF-8
Vinverse to prosty filtr do usuwania (resztkowego) efektu grzebienia,
oparty na skrypcie AviSynth autorstwa Didée
<http://forum.doom9.org/showthread.php?p=841641#post841641>.

%prep
%setup -q -n vs-vinverse-obsolete-%{gitref}

%build
libtool --tag=CC --mode=compile %{__cc} -c -o src/vinverse.lo %{rpmcflags} %{rpmcppflags} $(pkg-config --cflags vapoursynth) src/vinverse.c
libtool --tag=CC --mode=link %{__cc} -shared -module -avoid-version -o src/libvinverse.la %{rpmldflags} %{rpmcflags} src/vinverse.lo -rpath %{_libdir}/vapoursynth

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/vapoursynth

libtool --mode=install install src/libvinverse.la $RPM_BUILD_ROOT%{_libdir}/vapoursynth

%{__rm} $RPM_BUILD_ROOT%{_libdir}/vapoursynth/libvinverse.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/vinverse.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libvinverse.so
