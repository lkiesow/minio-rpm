%define debug_package %{nil}

%define  tag   RELEASE.2020-09-17T04-49-20Z
%define  stag  %(echo "%{tag}" | tr -d '-')
%define  uid   minio
%define  gid   minio
%define  nuid  975
%define  ngid  973

Name:          minio
Summary:       High performance object storage server compatible with Amazon S3 APIs
Version:       0.1.%{stag}
Release:       1%{?dist}
License:       ASL 2.0

Source0:       https://github.com/minio/minio/archive/%{tag}.tar.gz
Source1:       minio.service
Source2:       minio.conf
Source3:       https://raw.githubusercontent.com/minio/minio/%{tag}/LICENSE
URL:           https://min.io
BuildRoot:     %{_tmppath}/%{name}-root

BuildRequires:     git
BuildRequires:     golang
BuildRequires:     systemd
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

## Disable debug packages.
%define         debug_package %{nil}

## Go related tags.
%define         gobuild(o:) go build -tags=kqueue -trimpath -ldflags "${LDFLAGS:-}" %{?**};
%define         import_path     github.com/minio/minio

%description
The 100 percent Open Source, Enterprise-Grade,
Amazon S3 Compatible Object Storage

%prep
%setup -qc
mv %{name}-*/* .

install -d src/$(dirname %{import_path})
ln -s ../../.. src/%{import_path}



%build
# setup flags like 'go run buildscripts/gen-ldflags.go' would do
tag=%{tag}
version=${tag#RELEASE.}
prefix=%{import_path}/cmd

LDFLAGS="-X $prefix.Version=$version -X $prefix.ReleaseTag=$tag"

%gobuild -o %{name} %{import_path}

%install
rm -rf %{buildroot}

install -p -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/certs/
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/minio

# install binary
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

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
      useradd -M -r -s /sbin/nologin -u %{nuid} -d %{_sharedstatedir}/minio -g %{gid} %{uid} > /dev/null 2>&1 || :
   else
      useradd -M -r -s /sbin/nologin -d %{_sharedstatedir}/minio -g %{gid} %{uid} > /dev/null 2>&1 || :
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
* Fri Sep 18 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200917T044920Z-1
- Update to RELEASE.2020-09-17T04-49-20Z

* Thu Sep 17 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200916T042235Z-1
- Update to RELEASE.2020-09-16T04-22-35Z

* Fri Sep 11 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200910T220245Z-1
- Update to RELEASE.2020-09-10T22-02-45Z

* Wed Sep 09 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200908T230518Z-1
- Update to RELEASE.2020-09-08T23-05-18Z

* Sun Sep 06 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200905T071449Z-1
- Update to RELEASE.2020-09-05T07-14-49Z

* Thu Sep 03 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200902T181950Z-1
- Update to RELEASE.2020-09-02T18-19-50Z

* Fri Aug 28 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200827T051620Z-1
- Update to RELEASE.2020-08-27T05-16-20Z

* Thu Aug 27 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200826T000049Z-1
- Update to RELEASE.2020-08-26T00-00-49Z

* Wed Aug 26 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200825T002120Z-1
- Update to RELEASE.2020-08-25T00-21-20Z

* Wed Aug 19 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200818T194100Z-1
- Update to RELEASE.2020-08-18T19-41-00Z

* Mon Aug 17 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200816T183938Z-1
- Update to RELEASE.2020-08-16T18-39-38Z

* Fri Aug 14 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200813T023950Z-1
- Update to RELEASE.2020-08-13T02-39-50Z

* Sun Aug 09 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200808T045006Z-1
- Update to RELEASE.2020-08-08T04-50-06Z

* Sat Aug 08 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200807T012307Z-1
- Update to RELEASE.2020-08-07T01-23-07Z

* Thu Aug 06 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200805T213413Z-1
- Update to RELEASE.2020-08-05T21-34-13Z

* Wed Aug 05 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200804T231051Z-1
- Update to RELEASE.2020-08-04T23-10-51Z

* Sat Aug 01 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200731T033905Z-1
- Update to RELEASE.2020-07-31T03-39-05Z

* Tue Jul 28 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200727T183702Z-1
- Update to RELEASE.2020-07-27T18-37-02Z

* Sun Jul 26 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200724T224305Z-1
- Update to RELEASE.2020-07-24T22-43-05Z

* Thu Jul 23 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200722T002633Z-1
- Update to RELEASE.2020-07-22T00-26-33Z

* Tue Jul 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200720T022516Z-1
- Update to RELEASE.2020-07-20T02-25-16Z

* Sun Jul 19 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200718T184816Z-1
- Update to RELEASE.2020-07-18T18-48-16Z

* Wed Jul 15 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200714T191430Z-1
- Update to RELEASE.2020-07-14T19-14-30Z

* Tue Jul 14 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200713T180956Z-1
- Update to RELEASE.2020-07-13T18-09-56Z

* Mon Jul 13 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200712T191417Z-1
- Update to RELEASE.2020-07-12T19-14-17Z

* Sun Jul 12 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200711T211423Z-1
- Update to RELEASE.2020-07-11T21-14-23Z

* Fri Jul 03 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200702T001509Z-1
- Update to RELEASE.2020-07-02T00-15-09Z

* Tue Jun 23 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200622T031250Z-1
- Update to RELEASE.2020-06-22T03-12-50Z

* Fri Jun 19 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200618T022335Z-1
- Update to RELEASE.2020-06-18T02-23-35Z

* Mon Jun 15 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200614T183217Z-1
- Update to RELEASE.2020-06-14T18-32-17Z

* Sat Jun 13 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200612T000619Z-1
- Update to RELEASE.2020-06-12T00-06-19Z

* Fri Jun 05 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200603T221349Z-1
- Update to RELEASE.2020-06-03T22-13-49Z

* Tue Jun 02 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200601T172803Z-1
- Update to RELEASE.2020-06-01T17-28-03Z

* Sat May 30 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200529T140849Z-1
- Update to RELEASE.2020-05-29T14-08-49Z

* Sun May 17 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200516T013321Z-1
- Update to RELEASE.2020-05-16T01-33-21Z

* Sat May 09 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200508T024049Z-1
- Update to RELEASE.2020-05-08T02-40-49Z

* Fri May 08 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200506T232325Z-1
- Update to RELEASE.2020-05-06T23-23-25Z

* Sat May 02 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200501T221914Z-1
- Update to RELEASE.2020-05-01T22-19-14Z

* Fri May 01 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200428T235656Z-1
- Update to RELEASE.2020-04-28T23-56-56Z

* Fri Apr 24 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200423T005849Z-1
- Update to RELEASE.2020-04-23T00-58-49Z

* Thu Apr 16 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200415T194218Z-1
- Update to RELEASE.2020-04-15T19-42-18Z

* Sat Apr 11 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200410T033442Z-1
- Update to RELEASE.2020-04-10T03-34-42Z

* Tue Apr 07 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200404T053931Z-1
- Update to RELEASE.2020-04-04T05-39-31Z

* Fri Apr 03 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200402T213449Z-1
- Update to RELEASE.2020-04-02T21-34-49Z

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
