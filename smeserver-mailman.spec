# $Id: smeserver-mailman.spec,v 1.10 2013/09/20 15:59:31 unnilennium Exp $
# Authority: gordonr
# Name: Gordon Rowell

# avoid brp bytecompile
%define __os_install_post %{nil}

Summary: Mailman configuration for SME server.
%define name smeserver-mailman
Name: %{name}
%define version 1.3.0
%define release 45
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
Requires: e-smith-release >= 8.0
Requires: mailman >= 2.1.9-20.el5.sme
Requires: e-smith-formmagick >= 1.4.0-12
BuildRequires: e-smith-devtools >= 1.13.1-03
Obsoletes: e-smith-mailman
Provides: e-smith-mailman
AutoReqProv: no

%description
Add Mailman integration to the SME server.

%changelog
* Fri Sep 20 2013 JP Pialasse <tests@pialasse.com> 1.3.0-45.sme
- fix bug [SME: 7787]

* Thu Sep 19 2013 JP Pialasse <tests@pialasse.com> 1.3.0-44.sme
- fix case sensitive TRUE to true in smeserver-mailman-1.3.0-restarthang.patch 
- wrong path to actions folder fixed
- see [SME: 7845]

* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.3.0-42.sme
- apply locale 2013-07-14 patch

* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.3.0-41.sme
- fix signal-event hang on mailman restart [SME ]
* Mon Jul 01 2013 JP Pialasse <tests@pialasse.com> 1.3.0-40.sme
- fix expanding pyc pyo [SME: 7730]

* Mon Jul 01 2013 JP Pialasse <tests@pialasse.com> 1.3.0-38.sme
- import to sme8 buildsys
- fix bootstrap hang [SME: 6693]

* Tue Mar 20 2012 SME Translation Server <translations@contribs.org> 1.3.0-37.el6
- apply locale 2012-03-20 patch

* Wed Apr 27 2011 SME Translation Server <translations@contribs.org> 1.3.0-36.sme
- apply locale 2011-04-27 patch

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 1.3.0-35.sme
- apply locale 2011-03-06 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 1.3.0-34.sme
- apply locale 2010-03-02 patch

* Tue Oct 27 2009 SME Translation Server <translations@contribs.org> 1.3.0-33.sme
- apply locale 2009-10-27 patch

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 1.3.0-32.sme
- apply locale 2009-08-24 patch

* Wed May 20 2009 SME Translation Server <translations@contribs.org> 1.3.0-31.sme
- apply locale 2009-05-20 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 1.3.0-30.sme
- apply locale 2009-04-27 patch

* Tue Mar 03 2009 SME Translation Server
- apply locale 2009-03-03 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-28
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Sat Jan 31 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-27
- Apply 31 Jan 2009 locale patch [SME: 4951]

* Wed Nov  5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-26
- Apply  5 Nov 2008 locale patch

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-25
- Apply 14 Oct 2008 locale patch

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.6-24
- Apply 1 July 2008 locale patch

* Fri Jun 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.6-23
- Apply 27 Jun 2008 locale patch

* Thu May 21 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.6-22
- Apply 21 May 2008 locale patch
- Fixed version number in previous changelog entry

* Mon May 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.6-21
- Apply 5 May 2008 locale patch

* Sat Apr 26 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-20
- Add common <base> tags to e-smith-formmagick's general

* Sat Apr 26 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-19
- Added 26 April 2008 locale patch

* Wed Apr 23 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-18
- Added 23 April 2008 locale patch
- Fixed changelog

* Wed Apr 23 2008 Daniel B. <daniel@firewall-services.com> 1.3.0-17
- Fix path for the archives [SME: 4252]

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.3.0-16
- Added 22 April 2008 locale patch

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Fri Sep 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-15
- Allow hyphen in list names in smelist command [SME: 1307]

* Fri Sep 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-14
- Add /sbin/e-smith/alias2mailman to convert hand-built alias files
  to mailman lists. Converst ~alias/.qmail-<listname> to the mailman
  list <listname>
- List owner is mailman{DefaultOwner} defaulting to admin

* Fri Sep 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-13
- Fix various permissions to satisfy /usr/lib/mailman/check_perms
- Update mailman dependency to latest from CentOS

* Wed Mar 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-12
- Run the addlist/rmlist actions before generic_template_expand [SME: 665]

* Wed Mar 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-11
- Ensure that mailman record exists prior to trying to set the status

* Wed Mar 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-10
- Adjust path in post-install script to match CentOS structure

* Wed Mar 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-09
- Make further use of services2adjust and templates2expand

* Wed Mar 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-08
- Make use of services2adjust and templates2expand
- Update dependency as this is for 7.0

* Wed Mar 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-07
- Create qfiles heirarchy
- Fix up taint issue in smelist script

* Thu Jan 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-06
- TODO: Check permissions on /var/spool/mailman/qfiles. The 
  'in' directory needs to be writable by the mailman CGI script,
  which is running as www.

* Thu Jan 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-05
- Remove postun section which depended on action scripts which
  no longer exist

* Fri Dec 23 2005 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-04
- Allow mail for mailman user
- TODO: We should have configurable allow/deny for system accounts

* Tue Oct 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-03
- No change
- TODO: Rewrite templates to new API and move to templates2expand
- TODO: Add pre script to relocate /opt/mailman parts for upgrades

* Tue Oct 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-02
- Require patched mailman - SME Server runs httpd as www, not apache
- Relocate paths from /opt/mailman to /usr/lib/mailman to match mailman pkg
- Changed references to accounts db to new location

* Tue Oct 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.3.0-01
- Package renamed to smeserver-mailman, including patches to 1.1.10-05
- TODO: Relocate to /usr/lib/mailman
- TODO: Change DB references, and rewrite to new API

* Fri Oct 14 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.10-05]
- Fixed error with creation of alias file with dot in the name.

* Wed Mar 16 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.10-04]
- Added FQDN of box as a potential virtual host.

* Mon Mar 14 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.10-03]
- Removed circular event call. 

* Wed Feb 23 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.10-02]
- Forgot to set mode on smelist. 

* Wed Feb 16 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.10-01]
- Added hooks into domain creation and deletion.

* Wed Feb 16 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.9-01]
- Rolling again to get past build error on sme61build.

* Wed Feb 16 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.8-01]
- Added create-system-user call to make the mailman user. 
- Added a link to the mailman UI.

* Tue Feb 15 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.7-01]
- Updated mailman-conf to call a post-install script when first run. If this
  is ever included in a blade, post-install should move to the blade handler.

* Tue Feb 15 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.6-01]
- Fixed badly placed lib.
- Added post-install script to move it out of scriptlets.

* Tue Feb 15 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.5-01]
- Added conf and restart actions. 
- Added a simple panel.

* Tue Feb 15 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.4-01]
- Fixed perms on /opt/mailman, and bad symlink.

* Sun Feb 13 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.3-01]
- Fixed error in createlinks.

* Sun Feb 13 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.2-01]
- Rolling initial build of imported package. [msoulier]

* Sun Feb 13 2005 Michael Soulier <msoulier@e-smith.com>
- [1.1.1-01]
- Reimplementation after lost packages. Implementing for mailman 2.1.5.
  [msoulier]

* Sun Sep 08 2002 Shad L. Lords <slords@mail.com>
- 1.0-5
- updated addlist and rmlist to better handle conflicts

* Sun Sep 01 2002 Shad L. Lords <slords@mail.com>
- 1.0-4
- updated accounts so that ezmlm can coexist with mailman

* Tue Aug 27 2002 Shad L. Lords <slords@mail.com>
- 1.0-3
- make site have a random password on install
- make mailman list have random password on install

* Sat Aug 24 2002 Shad L. Lords <slords@mail.com>
- 1.0-2
- changed mailman-addlist to set perms and ownership correctly.
- changed permissions from root,mailman to mailman,mailman

* Fri Aug 23 2002 Shad L. Lords <slords@mail.com>
- 1.0-1
- Initial release

%prep
%setup

/bin/rm -r root/opt/mailman

%build
perl createlinks
mkdir -p root/usr/lib/mailman/aliases

mkdir -p root/opt
ln -s /usr/lib/mailman root/opt/mailman
mkdir -p root/var/spool/mailman/qfiles
for dir in archive bounces commands in news out retry shunt virgin
do
    mkdir -p root/var/spool/mailman/qfiles/$dir
done


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f e-smith-%{version}-filelist
/sbin/e-smith/genfilelist \
    --dir '/usr/lib/mailman' 'attr(02775,root,mailman)' \
    --dir '/usr/lib/mailman/bin' 'attr(02775,root,mailman)' \
    --dir '/var/spool/mailman' 'attr(02775,root,mailman)' \
    --dir '/usr/lib/mailman/aliases' 'attr(02775,mailman,mailman)' \
    --file '/usr/lib/mailman/bin/post-install' 'attr(0755,root,mailman)' \
    --file '/usr/lib/mailman/bin/smelist' 'attr(04755,root,mailman)' \
    --dir '/usr/lib/mailman/Mailman' 'attr(02775,root,mailman)' \
    --dir '/usr/lib/mailman/Mailman/MTA' 'attr(02775,root,mailman)' \
    --file '/usr/lib/mailman/Mailman/MTA/SME.py' 'attr(02775,root,mailman)' \
    --dir  '/var/spool/mailman/qfiles' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/archive' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/bounces' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/commands' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/in' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/news' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/out' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/retry' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/shunt' 'attr(02770,mailman,mailman)' \
    --dir  '/var/spool/mailman/qfiles/virgin' 'attr(02770,mailman,mailman)' \
    $RPM_BUILD_ROOT > %{name}-%{version}-filelist

# SME8 build to avoid error 
#/usr/lib/rpm/brp-python-bytecompile
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/domain-create/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyc
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/domain-create/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyo
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/domain-delete/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyc
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/domain-delete/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyo
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/bootstrap-console-save/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyc
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/bootstrap-console-save/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyo
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/mailman-update/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyc
#rm -rf $RPM_BUILD_ROOT/etc/e-smith/events/mailman-update/templates2expand/usr/lib/mailman/Mailman/mm_cfg.pyo 
#rm -rf $RPM_BUILD_ROOT/usr/lib/mailman/Mailman/mm_cfg.pyc
#rm -rf $RPM_BUILD_ROOT/usr/lib/mailman/Mailman/mm_cfg.pyo
#rm -rf $RPM_BUILD_ROOT/usr/lib/mailman/Mailman/MTA/SME.pyc
#rm -rf $RPM_BUILD_ROOT/usr/lib/mailman/Mailman/MTA/SME.pyo

# fixe for unwanted listed compiled python files
cat %{name}-%{version}-filelist |sed '/py[oc]$/d'>%{name}-%{version}-filelist.tmp
cat %{name}-%{version}-filelist.tmp> %{name}-%{version}-filelist
#rm -rf %{name}-%{version}-filelist.tmp

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist

%defattr(-,root,root)

%pre
/sbin/e-smith/create-system-user mailman 41 \
    "Mailman user" /usr/lib/mailman /bin/false

%post

%preun

%postun
