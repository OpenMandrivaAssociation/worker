%define name worker
%define version 2.17.10
%define release %mkrel 3
%define docver 2.10.0.2

Summary: A file manager for X in AMIGA style
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.boomerangsworld.de/cms/worker/downloads/%{name}-%{version}.tar.bz2
Source1: worker-%docver-doc.tar.bz2
Source3: %{name}-48.png
Source4: %{name}-32.png
Source5: %{name}-16.png
License: GPLv2+
Group: File tools
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.boomerangsworld.de/worker
BuildRequires: libx11-devel
BuildRequires: magic-devel

%description
Worker is a graphical filemanager for the X Window System.
It use the classical two-panel-view of the files and directories. 
It hast many intern operations while any extern program can also be
used for operate on the selected items. You can easily add actions 
to filetypes or buttons with the builtin configuration program.

%prep
%setup -q -a 1

%build
%configure2_5x
%make

pushd %name-%docver-doc
%configure2_5x
%make
popd

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%makeinstall_std -C %name-%docver-doc

mkdir -p $RPM_BUILD_ROOT{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/*
%_datadir/applications/*.desktop
%{_datadir}/worker
%{_mandir}/man1/worker.1*
%lang(fr) %{_mandir}/fr/man1/worker.1.*
%lang(it) %{_mandir}/it/man1/worker.1.*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%_datadir/pixmaps/*.xpm
