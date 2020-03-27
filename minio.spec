%define debug_package %{nil}

%define  tag   RELEASE.2020-03-25T07-03-04Z
%define  stag  %(echo "%{tag}" | tr -d '-')
%define  uid   minio
%define  gid   minio
%define  nuid  7969
%define  ngid  7969

Name:          minio
Summary:       High performance object storage server compatible with Amazon S3 APIs
Version:       0.1.%{stag}
Release:       1%{?dist}
License:       ASL 2.0

Source0:       https://dl.min.io/server/minio/release/linux-amd64/archive/%{name}.%{tag}
Source1:       https://raw.githubusercontent.com/lkiesow/minio-rpm/master/minio.service
Source2:       https://raw.githubusercontent.com/lkiesow/minio-rpm/master/minio.conf
Source3:       https://raw.githubusercontent.com/minio/minio/%{tag}/LICENSE
URL:           https://min.io
BuildRoot:     %{_tmppath}/%{name}-root

BuildRequires:     systemd
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd


%description
The 100 percent Open Source, Enterprise-Grade,
Amazon S3 Compatible Object Storage


%prep

%build

%install
rm -rf %{buildroot}

install -p -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/certs/
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/minio

# install binary
install -p -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

# install unit file
install -p -D -m 0644 \
   %{SOURCE1} \
   %{buildroot}%{_unitdir}/minio.service

# install configuration
install -p -D -m 0644 \
   %{SOURCE2} \
   %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

# license
cp %{SOURCE3} .


%clean
rm -rf %{buildroot}


%pre
# Create user and group if nonexistent
# Try using a common numeric uid/gid if possible
if [ ! $(getent group %{gid}) ]; then
   if [ ! $(getent group %{ngid}) ]; then
      groupadd -r -g %{ngid} %{gid} > /dev/null 2>&1 || :
   else
      groupadd -r %{gid} > /dev/null 2>&1 || :
   fi
fi
if [ ! $(getent passwd %{uid}) ]; then
   if [ ! $(getent passwd %{nuid}) ]; then
      useradd -M -r -u %{nuid} -d %{_sharedstatedir}/minio -g %{gid} %{uid} > /dev/null 2>&1 || :
   else
      useradd -M -r -d %{_sharedstatedir}/minio -g %{gid} %{uid} > /dev/null 2>&1 || :
   fi
fi


%post
%systemd_post minio.service


%preun
%systemd_preun minio.service


%postun
%systemd_postun_with_restart minio.service


%files
%defattr(-,root,root,-)
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/minio
%{_unitdir}/minio.service
%attr(755,%{uid},%{gid}) %dir %{_sharedstatedir}/minio
%license LICENSE


%changelog
* Sat Mar 28 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200325T070304Z-1
- Update to RELEASE.2020-03-25T07-03-04Z

* Sun Mar 22 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200319T214900Z-1
- Update to RELEASE.2020-03-19T21-49-00Z

* Sun Mar 15 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200314T022158Z-1
- Update to RELEASE.2020-03-14T02-21-58Z

* Sat Mar 07 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200306T222356Z-1
- Update to RELEASE.2020-03-06T22-23-56Z

* Thu Mar 05 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200305T010419Z-1
- Update to RELEASE.2020-03-05T01-04-19Z

* Sun Mar 01 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200227T002305Z-1
- Update to RELEASE.2020-02-27T00-23-05Z

* Fri Feb 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200220T225123Z-1
- Update to RELEASE.2020-02-20T22-51-23Z

* Sat Feb 08 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200207T232816Z-1
- Update to RELEASE.2020-02-07T23-28-16Z

* Mon Jan 27 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200125T025051Z-1
- Update to RELEASE.2020-01-25T02-50-51Z

* Fri Jan 17 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200116T224029Z-1
- Update to RELEASE.2020-01-16T22-40-29Z

* Sun Jan 05 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200103T191221Z-1
- Update to RELEASE.2020-01-03T19-12-21Z

* Tue Dec 31 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191230T054539Z-1
- Update to RELEASE.2019-12-30T05-45-39Z

* Thu Dec 26 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191224T230445Z-1
- Update to RELEASE.2019-12-24T23-04-45Z

* Fri Dec 20 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191219T225226Z-1
- Update to RELEASE.2019-12-19T22-52-26Z

* Wed Dec 18 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191217T231633Z-2
- Update to RELEASE.2019-12-17T23-16-33Z

* Fri Oct 25 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191012T013957Z-2
- Fixed home directory
- Fixed systemd unit configuration

* Sun Oct 13 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191012T013957Z-1
- Update to RELEASE.2019-10-12T01-39-57Z

* Fri Oct 04 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191002T211938Z-1
- Update to RELEASE.2019-10-02T21-19-38Z

* Sun Sep 08 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20190905T232438Z-1
- Update to RELEASE.2019-09-05T23-24-38Z

* Tue Aug 20 2019 Lars Kiesow <lkiesow@uos.de> 0.1.RELEASE.20190814T203741Z-1
- initial build
