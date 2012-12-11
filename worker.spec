%define name worker
%define version 2.19.1
%define release %mkrel 1
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


%changelog
* Mon Feb 20 2012 Götz Waschk <waschk@mandriva.org> 2.19.1-1mdv2012.0
+ Revision: 777870
- update to new version 2.19.1

* Wed Feb 01 2012 Götz Waschk <waschk@mandriva.org> 2.19.0-1
+ Revision: 770417
- new version

* Sat Jun 04 2011 Funda Wang <fwang@mandriva.org> 2.17.13-1
+ Revision: 682728
- update to new version 2.17.13

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.17.12-1
+ Revision: 680636
- update to new version 2.17.12

* Sat Mar 05 2011 Funda Wang <fwang@mandriva.org> 2.17.10-3
+ Revision: 642114
- rebuild

* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 2.17.10-2
+ Revision: 635644
- tighten BR

* Tue Feb 01 2011 Götz Waschk <waschk@mandriva.org> 2.17.10-1
+ Revision: 634650
- new version
- use upstream desktop entry

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 2.17.8-1mdv2011.0
+ Revision: 550287
- update to new version 2.17.8

* Thu Mar 04 2010 Frederik Himpe <fhimpe@mandriva.org> 2.17.6-1mdv2010.1
+ Revision: 514237
- update to new version 2.17.6

* Thu Nov 12 2009 Götz Waschk <waschk@mandriva.org> 2.17.5-1mdv2010.1
+ Revision: 465163
- new version
- drop patch

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 2.17.2-2mdv2010.0
+ Revision: 445818
- rebuild

* Mon Mar 09 2009 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2009.1
+ Revision: 353199
- new version
- fix build

* Sat Feb 21 2009 Götz Waschk <waschk@mandriva.org> 2.17.1-1mdv2009.1
+ Revision: 343743
- update to new version 2.17.1

* Fri Jul 04 2008 Götz Waschk <waschk@mandriva.org> 2.16.5-1mdv2009.0
+ Revision: 231549
- new version

* Wed Jul 02 2008 Götz Waschk <waschk@mandriva.org> 2.16.4-1mdv2009.0
+ Revision: 230605
- new version
- update license

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.16.2-1mdv2008.1
+ Revision: 165857
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2008.1
+ Revision: 115382
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - buildrequires X11-devel instead of XFree86-devel
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jun 29 2007 Funda Wang <fwang@mandriva.org> 2.15.0-1mdv2008.0
+ Revision: 45633
- New version


* Thu Mar 22 2007 Götz Waschk <waschk@mandriva.org> 2.14.4-1mdv2007.1
+ Revision: 148181
- new version
- new version
- new docs

* Fri Dec 01 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-2mdv2007.1
+ Revision: 89597
- rebuild

* Tue Nov 14 2006 Lenny Cartier <lenny@mandriva.com> 2.14.1-1mdv2007.1
+ Revision: 84031
- Update to 2.14.1
- Import worker

* Wed Sep 13 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdv2007.0
- New version 2.14.0

* Sat Jul 22 2006 G�tz Waschk <waschk@mandriva.org> 2.13.1-1mdv2007.0
- xdg menu
- New release 2.13.1

* Fri Jun 23 2006 Götz Waschk <waschk@mandriva.org> 2.13.0-1mdv2007.0
- New release 2.13.0

* Fri May 05 2006 Lenny Cartier <lenny@mandriva.com> 2.12.0-1mdk
- 2.12

* Tue Mar 07 2006 G�tz Waschk <waschk@mandriva.org> 2.11.2-1mdk
- update URL
- new version

* Thu Dec 15 2005 Götz Waschk <waschk@mandriva.org> 2.11.1-1mdk
- New release 2.11.1
- use mkrel

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 2.11.0-1mdk
- New release 2.11.0

* Wed Jul 27 2005 G�tz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- New release 2.10.2

* Sat Jun 25 2005 G�tz Waschk <waschk@mandriva.org> 2.10.1-1mdk
- New release 2.10.1

* Fri Apr 08 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.0-1mdk
- New release 2.10.0

* Tue Dec 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.9.0-1mdk
- 2.9.0

* Fri Jul 30 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.8.5-1mdk
- drop patch
- New release 2.8.5

* Fri Jun 18 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.8.4-2mdk
- patch for new g++

