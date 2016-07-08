Name:    kaffeine
Version: 2.0.4
Release: 3%{?dist}

License: GPLv2+
Summary: KDE media player
Group:   Applications/Multimedia
URL:     http://kaffeine.kde.org/
Source0: http://download.kde.org/%{stable}/%{name}/%{version}/src/%{name}-%{version}.tar.xz
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(libdvbv5)
BuildRequires: pkgconfig(xscrnsaver)

%{?kf5_kinit_requires}
Requires: kio-extras

%description
Kaffeine is a KDE Frameworks media player.


%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-qt --with-man --all-name


%check
desktop-file-validate %{buildroot}/%{_kf5_datadir}/applications/org.kde.kaffeine.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_kf5_datadir}/appdata/org.kde.kaffeine.appdata.xml


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_kf5_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
  /usr/bin/update-desktop-database &> /dev/null || :
  /bin/touch --no-create %{_kf5_datadir}/icons/hicolor &>/dev/null || :
  /usr/bin/gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_kf5_bindir}/kaffeine
%{_kf5_bindir}/dtvdaemon
%{_kf5_datadir}/kaffeine/
%{_kf5_datadir}/solid/actions/*.desktop
%{_kf5_datadir}/applications/org.kde.kaffeine.desktop
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/appdata/org.kde.kaffeine.appdata.xml
%{_kf5_datadir}/profiles/kaffeine.profile.xml
%{_kf5_docdir}/HTML/*/kaffeine/
%{_kf5_mandir}/man1/kaffeine.1.*

%changelog
* Fri Jul 08 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-3
- use kinit requires macro

* Thu Jul 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-2
- add some missing runtime deps

* Thu Jul 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-1
- update to 2.0.4 release

* Mon Jun 27 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-9
- Patch for gcc6 and cmake changes

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Oct 23 2013 Xavier Bachelot <xavier@bachelot.org> - 1.2.2-7
- Rebuild for xine-lib 1.2.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.2.2-3
- backport upstream patch to fix FTBFS with g++ 4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 09 2011 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-1
- 1.2.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 06 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.1-1
- kaffeine 1.1
- fixes #618718

* Tue Aug 17 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0-7
- reverted to source

* Tue Aug 17 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0-6
- use ln now to have a kaffeine icon in hicolor
- working with upstream to get it fixed
- fixes #611273

* Sun Jul 04 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0-5
- changed Requires to kdebase-runtime
- added kaffeine.png to fix #611273

* Sun Jul 04 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0-4
- added Requires oxygen-icon-theme

* Mon Jun 21 2010 Rex Dieter <rdieter@fedoraproject.org> 1.0-3
- Unexpanded macro in kdelibs4 dependency (#606134)
- remove old/unused patches

* Tue Jun 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0-2
- removed Require libXss, added BR libXss-devel

* Tue Jun 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0-1
- kaffeine 1.0
- new dep libXss
- lots of improvements and bugfixes

* Thu Apr 15 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0-0.5.pre3
- deinterlace-optional patch thanks to Kevin Kofler

* Mon Feb 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0-0.4.pre3
- kaffeine-1.0-pre3
- adjust summary/description: no longer phonon based (uses xine-lib)

* Fri Aug 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0-0.3.pre2
- kaffeine-1.0-pre2
- update %%description/%%summary
- %%check: use desktop-file-validate

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0-0.1.pre1
- kaffeine-1.0-pre1 

* Sun Apr 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.7-7
- re-enable dvb (#495379)

* Wed Mar 18 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.8.7-6
- Improve icon cache and desktop database update scriptlets.
- Update URL.

* Fri Mar 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.8.7-5
- s/nonfree/freeworld/
- --without-dvb (f11+)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Jussi Torhonen <jt at iki.fi> - 0.8.7-3
- EPG and OSD patch (#452421).

* Thu Aug 28 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.8.7-2
- Unfuzz optflags patch.

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8.7-1
- kaffeine-0.8.7

* Thu Mar 20 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.8.6-4
- Patch to apply $RPM_OPT_FLAGS when building DVB libs.

* Fri Mar 07 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8.6-3
- fix deps wrt kaffeine-libs (#436442)
- f7: xcb support (#373411)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.6-2
- Autorebuild for GCC 4.3

* Sun Jan 20 2008 Rex Dieter <rdieter@fedoraproject.org> 0.8.6-1
- kaffeine-0.8.6

* Sun Jan 13 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.8.5-7
- Require kdelibs3-devel instead of kdelibs-devel in -devel.

* Sat Dec 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.5-6
- BR: kdelibs3-devel

* Tue Oct 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.5-5
- multiarch conflicts in kaffeine (#341681)

* Wed Sep 19 2007 Ville Skyttä <ville.skytta at iki.fi> 0.8.5-4
- Avoid autotools re-run after configure (unclean upstream tarball?)

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.5-3
- respin (BuildID)

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.5-2
- License: GPLv2+
- BR: libxcb-devel (really)

* Mon Jul 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.5-1
- kaffeine-0.8.5
- BR: libxcb-devel

* Fri Jun 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.4-1
- kaffeine-0.8.4 (#243823)

* Thu Jan 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.8.3-4
- disable gst08 support (for now), it's been orphaned

* Wed Nov 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.3-3
- less globbing in %%files

* Wed Nov 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.3-2
- include libkaffeinepart.so in main pkg, not -devel (bug #217835)

* Sun Nov 26 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.3-1
- 0.8.3

* Sat Nov 04 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.2-6
- %%doc README

* Fri Nov 03 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.2-5
- fix chmod so it actually works.

* Thu Nov 02 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.2-4
- chmod -x AUTHORS ChangeLog TODO
- use rel symlinks under %%_docdir

* Wed Nov 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.2-3
- update %%description to not mention any specific mm containers 
  (like AVI, WMV).

* Wed Nov 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.2-2
- fixup for Extras
- support building kaffeine-extras-nonfree for that other repo. 

* Tue Sep 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.2-1
- 0.8.2

* Thu Aug 10 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-5
- for kdelibs >= 3.5.4, omit 
  /usr/share/mimelnk/application/x-mplayer2.desktop (lvn bug #1132)

* Thu May 18 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-4
- BR: libXtst-devel libXinerama-devel (fc5+)

* Tue Apr 25 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-3
- (re)enable gstreamer support (fc3+)

* Mon Apr 24 2006 Rex Dieter <rexdieter[AT]users.sf.net. 0.8.1-2
- avoid re-auto'ing thing, breaks locale/po-files

* Mon Apr 03 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.1-1
- 0.8.1
- cdda patch (upsgream bug #1463542)

* Sat Mar 25 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.7.1-4
- drop --vendor=livna
- fdo icon spec fix
- kaffeine-0.7.x-CVE-2006-0051.patch

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Thu Nov 03 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 0.7.1-0.lvn.3
- update-desktop-database (#645)
- -devel pkg (#645)
- -gstreamer subpkg, marked experimental (due to upstream #1254363)
- omit -desktop patch (#645)
- use desktop-file-install (#645)

* Wed Sep  7 2005 Thorsten Leemhuis <fedora at leemhuis.info> - 0:0.7.1-0.lvn.2
- configure with --with-qt-libraries=${QTDIR}/lib to fix build on x86_64

* Sun Sep  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.1-0.lvn.1
- 0.7.1, gcc visibility hack no longer needed.

* Mon Aug  8 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7-0.lvn.1
- 0.7, now with DVB support (FC4+ only).
- GStreamer support disabled by default due to upstream #1254363, rebuild
  with "--with gstreamer" to enable.
- Quick and dirty workaround for upstream #1253989.

* Sun Mar 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6-0.lvn.1
- 0.6.

* Thu Dec 23 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5-0.lvn.1
- Update to 0.5.

* Fri Nov  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5-0.lvn.0.1.rc2
- Update to 0.5rc2.

* Sun Oct  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5-0.lvn.0.1.rc1
- Update to 0.5rc1.
- Requires KDE >= 3.2 -> FC2 only -> make some related cleanups.
- Purge libselinux workarounds, no longer needed.
- Improve GNOME HIG compliance of desktop entry, sync with KPlayer (bug 173).
- Disable dependency tracking to speed up the build.
- Provide -devel.

* Sat May 22 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.lvn.1.b
- Update to 0.4.3b.
- Add workaround for https://bugzilla.redhat.com/123853

* Mon May  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.lvn.1
- Update to 0.4.3.

* Wed Mar 24 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.2-0.lvn.1
- Update to 0.4.2.

* Sat Jan 17 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.1-0.lvn.1
- Update to 0.4.1, patches applied upstream.
- Update description.

* Mon Nov 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4-0.lvn.1
- Update to 0.4.
- Disable rpath.
- Add Gnome icon.

* Tue Jul 29 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3.2-0.fdr.2
- Own directories under %%{_datadir}/icons.

* Tue Jul  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3.2-0.fdr.1
- First build.
