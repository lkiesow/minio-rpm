%define debug_package %{nil}

%define  tag   RELEASE.2022-02-12T00-51-25Z
%define  stag  %(echo "%{tag}" | tr -d '-')
%define  uid   minio
%define  gid   minio
%define  nuid  7969
%define  ngid  7969

Name:          minio
Summary:       High performance object storage server compatible with Amazon S3 APIs
Version:       0.1.%{stag}
Release:       2%{?dist}
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
* Mon Feb 14 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220212T005125Z-1
- Update to RELEASE.2022-02-12T00-51-25Z

* Tue Feb 08 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220207T081733Z-1
- Update to RELEASE.2022-02-07T08-17-33Z

* Sun Feb 06 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220205T044059Z-1
- Update to RELEASE.2022-02-05T04-40-59Z

* Wed Feb 02 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220201T180014Z-1
- Update to RELEASE.2022-02-01T18-00-14Z

* Sat Jan 29 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220128T022816Z-1
- Update to RELEASE.2022-01-28T02-28-16Z

* Fri Jan 28 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220127T035302Z-1
- Update to RELEASE.2022-01-27T03-53-02Z

* Wed Jan 26 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220125T195604Z-1
- Update to RELEASE.2022-01-25T19-56-04Z

* Sun Jan 09 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220108T031154Z-1
- Update to RELEASE.2022-01-08T03-11-54Z

* Sat Jan 08 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220107T015323Z-1
- Update to RELEASE.2022-01-07T01-53-23Z

* Wed Jan 05 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220104T074107Z-1
- Update to RELEASE.2022-01-04T07-41-07Z

* Thu Dec 30 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211229T064906Z-1
- Update to RELEASE.2021-12-29T06-49-06Z

* Tue Dec 28 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211227T072318Z-1
- Update to RELEASE.2021-12-27T07-23-18Z

* Tue Dec 21 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211220T220716Z-1
- Update to RELEASE.2021-12-20T22-07-16Z

* Mon Dec 20 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211218T044233Z-1
- Update to RELEASE.2021-12-18T04-42-33Z

* Sun Dec 12 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211210T230339Z-1
- Update to RELEASE.2021-12-10T23-03-39Z

* Fri Dec 10 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211209T061941Z-1
- Update to RELEASE.2021-12-09T06-19-41Z

* Fri Nov 26 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211124T231933Z-1
- Update to RELEASE.2021-11-24T23-19-33Z

* Wed Nov 10 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211109T032145Z-1
- Update to RELEASE.2021-11-09T03-21-45Z

* Sat Nov 06 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211105T091626Z-1
- Update to RELEASE.2021-11-05T09-16-26Z

* Thu Nov 04 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211103T033636Z-1
- Update to RELEASE.2021-11-03T03-36-36Z

* Fri Oct 29 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211027T162942Z-1
- Update to RELEASE.2021-10-27T16-29-42Z

* Thu Oct 28 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211023T032824Z-2
- Added MinIO Console port configuration

* Sun Oct 24 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211023T032824Z-1
- Update to RELEASE.2021-10-23T03-28-24Z

* Thu Oct 14 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211013T002317Z-1
- Update to RELEASE.2021-10-13T00-23-17Z

* Mon Oct 11 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211010T165330Z-1
- Update to RELEASE.2021-10-10T16-53-30Z

* Sun Oct 10 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211008T235824Z-1
- Update to RELEASE.2021-10-08T23-58-24Z

* Fri Oct 08 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211006T233631Z-1
- Update to RELEASE.2021-10-06T23-36-31Z

* Mon Oct 04 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211002T163105Z-1
- Update to RELEASE.2021-10-02T16-31-05Z

* Sat Sep 25 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210924T002424Z-1
- Update to RELEASE.2021-09-24T00-24-24Z

* Fri Sep 24 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210923T044624Z-1
- Update to RELEASE.2021-09-23T04-46-24Z

* Sun Sep 19 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210918T180959Z-1
- Update to RELEASE.2021-09-18T18-09-59Z

* Thu Sep 16 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210915T045425Z-1
- Update to RELEASE.2021-09-15T04-54-25Z

* Sat Sep 11 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210909T213707Z-1
- Update to RELEASE.2021-09-09T21-37-07Z

* Sat Sep 04 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210903T035613Z-1
- Update to RELEASE.2021-09-03T03-56-13Z

* Wed Sep 01 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210831T054654Z-1
- Update to RELEASE.2021-08-31T05-46-54Z

* Thu Aug 26 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210825T004118Z-1
- Update to RELEASE.2021-08-25T00-41-18Z

* Sun Aug 22 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210820T183201Z-1
- Update to RELEASE.2021-08-20T18-32-01Z

* Thu Aug 19 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210817T205308Z-1
- Update to RELEASE.2021-08-17T20-53-08Z

* Sat Aug 07 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210805T220119Z-1
- Update to RELEASE.2021-08-05T22-01-19Z

* Sat Jul 31 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210730T000200Z-1
- Update to RELEASE.2021-07-30T00-02-00Z

* Wed Jul 28 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210727T024015Z-1
- Update to RELEASE.2021-07-27T02-40-15Z

* Fri Jul 23 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210722T052332Z-1
- Update to RELEASE.2021-07-22T05-23-32Z

* Sat Jul 17 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210715T222734Z-1
- Update to RELEASE.2021-07-15T22-27-34Z

* Tue Jul 13 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210712T024453Z-1
- Update to RELEASE.2021-07-12T02-44-53Z

* Sat Jul 10 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210708T194325Z-1
- Update to RELEASE.2021-07-08T19-43-25Z

* Fri Jul 09 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210708T011501Z-1
- Update to RELEASE.2021-07-08T01-15-01Z

* Fri Jun 18 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210617T001046Z-1
- Update to RELEASE.2021-06-17T00-10-46Z

* Tue Jun 15 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210614T012923Z-1
- Update to RELEASE.2021-06-14T01-29-23Z

* Thu Jun 10 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210609T185139Z-1
- Update to RELEASE.2021-06-09T18-51-39Z

* Wed Jun 09 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210607T214051Z-1
- Update to RELEASE.2021-06-07T21-40-51Z

* Fri May 28 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210527T220631Z-1
- Update to RELEASE.2021-05-27T22-06-31Z

* Thu May 27 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210526T002246Z-1
- Update to RELEASE.2021-05-26T00-22-46Z

* Sun May 23 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210522T023439Z-1
- Update to RELEASE.2021-05-22T02-34-39Z

* Sat May 22 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210520T223144Z-1
- Update to RELEASE.2021-05-20T22-31-44Z

* Wed May 19 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210518T005328Z-1
- Update to RELEASE.2021-05-18T00-53-28Z

* Mon May 17 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210516T053234Z-1
- Update to RELEASE.2021-05-16T05-32-34Z

* Thu May 13 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210511T232741Z-1
- Update to RELEASE.2021-05-11T23-27-41Z

* Fri Apr 23 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210422T154428Z-1
- Update to RELEASE.2021-04-22T15-44-28Z

* Mon Apr 19 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210418T192629Z-1
- Update to RELEASE.2021-04-18T19-26-29Z

* Wed Apr 07 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210406T231100Z-1
- Update to RELEASE.2021-04-06T23-11-00Z

* Sat Mar 27 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210326T000041Z-1
- Update to RELEASE.2021-03-26T00-00-41Z

* Thu Mar 18 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210317T023302Z-1
- Update to RELEASE.2021-03-17T02-33-02Z

* Sat Mar 13 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210312T000047Z-1
- Update to RELEASE.2021-03-12T00-00-47Z

* Thu Mar 11 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210310T051133Z-1
- Update to RELEASE.2021-03-10T05-11-33Z

* Fri Mar 05 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210304T005313Z-1
- Update to RELEASE.2021-03-04T00-53-13Z

* Tue Mar 02 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210301T042055Z-1
- Update to RELEASE.2021-03-01T04-20-55Z

* Thu Feb 25 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210224T184445Z-1
- Update to RELEASE.2021-02-24T18-44-45Z

* Wed Feb 24 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210223T200501Z-1
- Update to RELEASE.2021-02-23T20-05-01Z

* Sat Feb 20 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210219T043802Z-1
- Update to RELEASE.2021-02-19T04-38-02Z

* Mon Feb 15 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210214T040133Z-1
- Update to RELEASE.2021-02-14T04-01-33Z

* Fri Feb 12 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210211T082343Z-1
- Update to RELEASE.2021-02-11T08-23-43Z

* Mon Feb 08 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210207T013102Z-1
- Update to RELEASE.2021-02-07T01-31-02Z

* Tue Feb 02 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210201T225652Z-1
- Update to RELEASE.2021-02-01T22-56-52Z

* Sun Jan 31 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210130T002058Z-1
- Update to RELEASE.2021-01-30T00-20-58Z

* Sun Jan 17 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210116T021944Z-1
- Update to RELEASE.2021-01-16T02-19-44Z

* Sat Jan 09 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210108T211821Z-1
- Update to RELEASE.2021-01-08T21-18-21Z

* Wed Jan 06 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210105T052238Z-1
- Update to RELEASE.2021-01-05T05-22-38Z

* Wed Dec 30 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201229T232929Z-1
- Update to RELEASE.2020-12-29T23-29-29Z

* Sun Dec 27 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201226T013554Z-1
- Update to RELEASE.2020-12-26T01-35-54Z

* Thu Dec 24 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201223T022412Z-1
- Update to RELEASE.2020-12-23T02-24-12Z

* Sat Dec 19 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201218T032742Z-1
- Update to RELEASE.2020-12-18T03-27-42Z

* Thu Dec 17 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201216T050517Z-1
- Update to RELEASE.2020-12-16T05-05-17Z

* Sun Dec 13 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201212T083907Z-1
- Update to RELEASE.2020-12-12T08-39-07Z

* Fri Dec 11 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201210T015429Z-1
- Update to RELEASE.2020-12-10T01-54-29Z

* Fri Dec 04 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201203T054924Z-1
- Update to RELEASE.2020-12-03T05-49-24Z

* Thu Nov 26 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201125T223625Z-1
- Update to RELEASE.2020-11-25T22-36-25Z

* Sat Nov 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201119T234816Z-1
- Update to RELEASE.2020-11-19T23-48-16Z

* Sat Nov 14 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201113T201018Z-1
- Update to RELEASE.2020-11-13T20-10-18Z

* Wed Nov 11 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201110T210224Z-1
- Update to RELEASE.2020-11-10T21-02-24Z

* Sun Nov 08 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201106T231707Z-1
- Update to RELEASE.2020-11-06T23-17-07Z

* Thu Oct 29 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201028T081650Z-1
- Update to RELEASE.2020-10-28T08-16-50Z

* Wed Oct 28 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201027T040355Z-1
- Update to RELEASE.2020-10-27T04-03-55Z

* Mon Oct 19 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201018T215412Z-1
- Update to RELEASE.2020-10-18T21-54-12Z

* Tue Oct 13 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201012T215321Z-1
- Update to RELEASE.2020-10-12T21-53-21Z

* Sat Oct 10 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201009T225505Z-1
- Update to RELEASE.2020-10-09T22-55-05Z

* Sun Oct 04 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201003T021942Z-1
- Update to RELEASE.2020-10-03T02-19-42Z

* Sun Sep 27 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200926T034456Z-1
- Update to RELEASE.2020-09-26T03-44-56Z

* Thu Sep 24 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200923T191830Z-1
- Update to RELEASE.2020-09-23T19-18-30Z

* Tue Sep 22 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200921T223159Z-1
- Update to RELEASE.2020-09-21T22-31-59Z

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
