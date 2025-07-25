%define debug_package %{nil}

%define  tag   RELEASE.2025-07-23T15-54-02Z
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
* Thu Jul 24 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250723T155402Z-1
- Update to RELEASE.2025-07-23T15-54-02Z

* Sat Jul 19 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250718T215631Z-1
- Update to RELEASE.2025-07-18T21-56-31Z

* Tue Jun 24 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250613T113347Z-1
- Update to RELEASE.2025-06-13T11-33-47Z

* Sun May 25 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250524T170830Z-1
- Update to RELEASE.2025-05-24T17-08-30Z

* Wed Apr 23 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250422T221226Z-1
- Update to RELEASE.2025-04-22T22-12-26Z

* Wed Apr 09 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250408T154124Z-1
- Update to RELEASE.2025-04-08T15-41-24Z

* Fri Apr 04 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250403T145628Z-1
- Update to RELEASE.2025-04-03T14-56-28Z

* Thu Mar 13 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250312T180418Z-1
- Update to RELEASE.2025-03-12T18-04-18Z

* Sat Mar 01 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250228T095516Z-1
- Update to RELEASE.2025-02-28T09-55-16Z

* Wed Feb 19 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250218T162555Z-1
- Update to RELEASE.2025-02-18T16-25-55Z

* Sun Feb 09 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250207T232109Z-1
- Update to RELEASE.2025-02-07T23-21-09Z

* Wed Feb 05 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250203T210304Z-1
- Update to RELEASE.2025-02-03T21-03-04Z

* Wed Jan 22 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250120T144907Z-1
- Update to RELEASE.2025-01-20T14-49-07Z

* Sun Jan 19 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250118T003137Z-1
- Update to RELEASE.2025-01-18T00-31-37Z

* Fri Dec 20 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241218T131544Z-1
- Update to RELEASE.2024-12-18T13-15-44Z

* Mon Dec 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241213T221912Z-1
- Update to RELEASE.2024-12-13T22-19-12Z

* Fri Nov 08 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241107T005220Z-1
- Update to RELEASE.2024-11-07T00-52-20Z

* Thu Oct 31 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241029T160148Z-1
- Update to RELEASE.2024-10-29T16-01-48Z

* Wed Oct 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241013T133411Z-1
- Update to RELEASE.2024-10-13T13-34-11Z

* Thu Oct 03 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241002T175041Z-1
- Update to RELEASE.2024-10-02T17-50-41Z

* Tue Sep 24 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240922T003343Z-1
- Update to RELEASE.2024-09-22T00-33-43Z

* Sun Sep 15 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240913T202602Z-1
- Update to RELEASE.2024-09-13T20-26-02Z

* Wed Sep 11 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240909T165928Z-1
- Update to RELEASE.2024-09-09T16-59-28Z

* Fri Aug 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240829T014052Z-1
- Update to RELEASE.2024-08-29T01-40-52Z

* Tue Aug 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240826T153307Z-1
- Update to RELEASE.2024-08-26T15-33-07Z

* Sun Aug 18 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240817T012454Z-1
- Update to RELEASE.2024-08-17T01-24-54Z

* Sun Aug 04 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240803T043323Z-1
- Update to RELEASE.2024-08-03T04-33-23Z

* Thu Aug 01 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240731T054626Z-1
- Update to RELEASE.2024-07-31T05-46-26Z

* Tue Jul 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240729T221452Z-1
- Update to RELEASE.2024-07-29T22-14-52Z

* Sun Jul 28 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240726T204821Z-1
- Update to RELEASE.2024-07-26T20-48-21Z

* Thu Jul 18 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240716T234641Z-1
- Update to RELEASE.2024-07-16T23-46-41Z

* Tue Jul 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240715T190230Z-1
- Update to RELEASE.2024-07-15T19-02-30Z

* Sun Jul 14 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240713T014615Z-1
- Update to RELEASE.2024-07-13T01-46-15Z

* Thu Jul 11 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240710T184149Z-1
- Update to RELEASE.2024-07-10T18-41-49Z

* Fri Jul 05 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240704T142545Z-1
- Update to RELEASE.2024-07-04T14-25-45Z

* Sun Jun 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240629T012047Z-1
- Update to RELEASE.2024-06-29T01-20-47Z

* Sat Jun 29 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240628T090649Z-1
- Update to RELEASE.2024-06-28T09-06-49Z

* Thu Jun 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240626T010618Z-1
- Update to RELEASE.2024-06-26T01-06-18Z

* Sun Jun 23 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240622T052645Z-1
- Update to RELEASE.2024-06-22T05-26-45Z

* Sat Jun 15 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240613T225353Z-1
- Update to RELEASE.2024-06-13T22-53-53Z

* Wed Jun 12 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240611T031330Z-1
- Update to RELEASE.2024-06-11T03-13-30Z

* Fri Jun 07 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240606T093642Z-1
- Update to RELEASE.2024-06-06T09-36-42Z

* Wed Jun 05 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240604T192008Z-1
- Update to RELEASE.2024-06-04T19-20-08Z

* Wed May 29 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240528T171904Z-1
- Update to RELEASE.2024-05-28T17-19-04Z

* Tue May 28 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240527T191746Z-1
- Update to RELEASE.2024-05-27T19-17-46Z

* Sat May 11 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240510T014138Z-1
- Update to RELEASE.2024-05-10T01-41-38Z

* Wed May 08 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240507T064125Z-1
- Update to RELEASE.2024-05-07T06-41-25Z

* Thu May 02 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240501T011110Z-1
- Update to RELEASE.2024-05-01T01-11-10Z

* Tue Apr 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240428T175350Z-1
- Update to RELEASE.2024-04-28T17-53-50Z

* Fri Apr 19 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240418T190919Z-1
- Update to RELEASE.2024-04-18T19-09-19Z

* Sun Apr 07 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240406T052602Z-1
- Update to RELEASE.2024-04-06T05-26-02Z

* Sun Mar 31 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240330T094156Z-1
- Update to RELEASE.2024-03-30T09-41-56Z

* Wed Mar 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240326T221045Z-1
- Update to RELEASE.2024-03-26T22-10-45Z

* Sat Mar 23 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240321T231343Z-1
- Update to RELEASE.2024-03-21T23-13-43Z

* Sat Mar 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240315T010719Z-1
- Update to RELEASE.2024-03-15T01-07-19Z

* Mon Mar 11 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240310T025348Z-1
- Update to RELEASE.2024-03-10T02-53-48Z

* Fri Mar 08 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240307T004348Z-1
- Update to RELEASE.2024-03-07T00-43-48Z

* Wed Mar 06 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240305T044844Z-1
- Update to RELEASE.2024-03-05T04-48-44Z

* Mon Mar 04 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240303T175039Z-1
- Update to RELEASE.2024-03-03T17-50-39Z

* Tue Feb 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240226T093348Z-1
- Update to RELEASE.2024-02-26T09-33-48Z

* Mon Feb 26 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240224T171114Z-1
- Update to RELEASE.2024-02-24T17-11-14Z

* Sun Feb 18 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240217T011557Z-1
- Update to RELEASE.2024-02-17T01-15-57Z

* Thu Feb 15 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240214T213602Z-1
- Update to RELEASE.2024-02-14T21-36-02Z

* Wed Feb 14 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240213T153511Z-1
- Update to RELEASE.2024-02-13T15-35-11Z

* Tue Feb 13 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240212T210227Z-1
- Update to RELEASE.2024-02-12T21-02-27Z

* Sat Feb 10 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240209T212516Z-1
- Update to RELEASE.2024-02-09T21-25-16Z

* Thu Feb 08 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240206T213622Z-1
- Update to RELEASE.2024-02-06T21-36-22Z

* Tue Feb 06 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240204T223613Z-1
- Update to RELEASE.2024-02-04T22-36-13Z

* Thu Feb 01 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240131T202033Z-1
- Update to RELEASE.2024-01-31T20-20-33Z

* Tue Jan 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240129T035632Z-1
- Update to RELEASE.2024-01-29T03-56-32Z

* Sat Jan 20 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240118T225128Z-1
- Update to RELEASE.2024-01-18T22-51-28Z

* Wed Jan 17 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240116T160738Z-1
- Update to RELEASE.2024-01-16T16-07-38Z

* Sun Jan 14 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240113T075303Z-1
- Update to RELEASE.2024-01-13T07-53-03Z

* Fri Jan 12 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240111T074616Z-1
- Update to RELEASE.2024-01-11T07-46-16Z

* Sun Jan 07 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240105T221724Z-1
- Update to RELEASE.2024-01-05T22-17-24Z

* Wed Jan 03 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240101T163633Z-1
- Update to RELEASE.2024-01-01T16-36-33Z

* Sun Dec 24 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231223T071911Z-1
- Update to RELEASE.2023-12-23T07-19-11Z

* Thu Dec 21 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231220T010002Z-1
- Update to RELEASE.2023-12-20T01-00-02Z

* Fri Dec 15 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231214T185157Z-1
- Update to RELEASE.2023-12-14T18-51-57Z

* Sun Dec 10 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231209T181751Z-1
- Update to RELEASE.2023-12-09T18-17-51Z

* Fri Dec 08 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231207T041600Z-1
- Update to RELEASE.2023-12-07T04-16-00Z

* Thu Dec 07 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231206T090922Z-1
- Update to RELEASE.2023-12-06T09-09-22Z

* Sun Dec 03 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231202T105133Z-1
- Update to RELEASE.2023-12-02T10-51-33Z

* Wed Nov 22 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231120T224007Z-1
- Update to RELEASE.2023-11-20T22-40-07Z

* Fri Nov 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231115T204325Z-1
- Update to RELEASE.2023-11-15T20-43-25Z

* Sun Nov 12 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231111T081441Z-1
- Update to RELEASE.2023-11-11T08-14-41Z

* Thu Nov 09 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231106T222608Z-1
- Update to RELEASE.2023-11-06T22-26-08Z

* Thu Nov 02 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231101T183725Z-1
- Update to RELEASE.2023-11-01T18-37-25Z

* Thu Oct 26 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231025T063325Z-1
- Update to RELEASE.2023-10-25T06-33-25Z

* Wed Oct 25 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231024T044236Z-1
- Update to RELEASE.2023-10-24T04-42-36Z

* Tue Oct 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231016T041343Z-1
- Update to RELEASE.2023-10-16T04-13-43Z

* Sun Oct 15 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231014T051722Z-1
- Update to RELEASE.2023-10-14T05-17-22Z

* Mon Oct 09 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231007T150738Z-1
- Update to RELEASE.2023-10-07T15-07-38Z

* Sun Oct 01 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230930T070229Z-1
- Update to RELEASE.2023-09-30T07-02-29Z

* Fri Sep 29 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230927T152250Z-1
- Update to RELEASE.2023-09-27T15-22-50Z

* Tue Sep 26 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230923T034750Z-1
- Update to RELEASE.2023-09-23T03-47-50Z

* Fri Sep 22 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230920T224955Z-1
- Update to RELEASE.2023-09-20T22-49-55Z

* Sun Sep 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230916T010147Z-1
- Update to RELEASE.2023-09-16T01-01-47Z

* Fri Sep 08 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230907T020502Z-1
- Update to RELEASE.2023-09-07T02-05-02Z

* Tue Sep 05 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230904T195737Z-1
- Update to RELEASE.2023-09-04T19-57-37Z

* Fri Sep 01 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230831T153116Z-1
- Update to RELEASE.2023-08-31T15-31-16Z

* Thu Aug 31 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230829T230735Z-1
- Update to RELEASE.2023-08-29T23-07-35Z

* Thu Aug 24 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230823T100706Z-1
- Update to RELEASE.2023-08-23T10-07-06Z

* Thu Aug 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230816T201730Z-1
- Update to RELEASE.2023-08-16T20-17-30Z

* Thu Aug 10 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230809T233022Z-1
- Update to RELEASE.2023-08-09T23-30-22Z

* Sat Aug 05 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230804T174021Z-1
- Update to RELEASE.2023-08-04T17-40-21Z

* Sat Jul 22 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230721T211244Z-1
- Update to RELEASE.2023-07-21T21-12-44Z

* Wed Jul 19 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230718T174940Z-1
- Update to RELEASE.2023-07-18T17-49-40Z

* Wed Jul 12 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230711T212934Z-1
- Update to RELEASE.2023-07-11T21-29-34Z

* Sat Jul 08 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230707T071357Z-1
- Update to RELEASE.2023-07-07T07-13-57Z

* Fri Jun 30 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230629T051228Z-1
- Update to RELEASE.2023-06-29T05-12-28Z

* Sun Jun 25 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230623T202600Z-1
- Update to RELEASE.2023-06-23T20-26-00Z

* Tue Jun 20 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230619T195250Z-1
- Update to RELEASE.2023-06-19T19-52-50Z

* Sat Jun 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230616T024106Z-1
- Update to RELEASE.2023-06-16T02-41-06Z

* Sun Jun 11 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230609T073212Z-1
- Update to RELEASE.2023-06-09T07-32-12Z

* Sun Jun 04 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230602T231726Z-1
- Update to RELEASE.2023-06-02T23-17-26Z

* Mon May 29 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230527T055619Z-1
- Update to RELEASE.2023-05-27T05-56-19Z

* Fri May 19 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230518T000536Z-1
- Update to RELEASE.2023-05-18T00-05-36Z

* Sat May 06 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230504T214430Z-1
- Update to RELEASE.2023-05-04T21-44-30Z

* Sat Apr 29 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230428T181117Z-1
- Update to RELEASE.2023-04-28T18-11-17Z

* Sat Apr 22 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230420T175655Z-1
- Update to RELEASE.2023-04-20T17-56-55Z

* Fri Apr 14 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230413T030807Z-1
- Update to RELEASE.2023-04-13T03-08-07Z

* Sat Apr 08 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230407T052858Z-1
- Update to RELEASE.2023-04-07T05-28-58Z

* Sat Mar 25 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230324T214123Z-1
- Update to RELEASE.2023-03-24T21-41-23Z

* Thu Mar 23 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230322T063624Z-1
- Update to RELEASE.2023-03-22T06-36-24Z

* Tue Mar 21 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230320T201618Z-1
- Update to RELEASE.2023-03-20T20-16-18Z

* Tue Mar 14 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230313T194617Z-1
- Update to RELEASE.2023-03-13T19-46-17Z

* Sat Mar 11 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230309T231613Z-1
- Update to RELEASE.2023-03-09T23-16-13Z

* Tue Feb 28 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230227T181045Z-1
- Update to RELEASE.2023-02-27T18-10-45Z

* Thu Feb 23 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230222T182345Z-1
- Update to RELEASE.2023-02-22T18-23-45Z

* Sat Feb 18 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230217T175243Z-1
- Update to RELEASE.2023-02-17T17-52-43Z

* Sat Feb 11 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230210T184839Z-1
- Update to RELEASE.2023-02-10T18-48-39Z

* Fri Feb 10 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230209T051653Z-1
- Update to RELEASE.2023-02-09T05-16-53Z

* Wed Feb 01 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230131T022419Z-1
- Update to RELEASE.2023-01-31T02-24-19Z

* Thu Jan 26 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230125T001954Z-1
- Update to RELEASE.2023-01-25T00-19-54Z

* Sat Jan 21 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230120T020544Z-1
- Update to RELEASE.2023-01-20T02-05-44Z

* Thu Jan 19 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230118T043638Z-1
- Update to RELEASE.2023-01-18T04-36-38Z

* Fri Jan 13 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230112T020616Z-1
- Update to RELEASE.2023-01-12T02-06-16Z

* Mon Jan 09 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230106T181118Z-1
- Update to RELEASE.2023-01-06T18-11-18Z

* Wed Jan 04 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230102T094009Z-1
- Update to RELEASE.2023-01-02T09-40-09Z

* Wed Dec 14 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221212T192727Z-1
- Update to RELEASE.2022-12-12T19-27-27Z

* Thu Dec 08 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221207T005637Z-1
- Update to RELEASE.2022-12-07T00-56-37Z

* Sat Dec 03 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221202T191922Z-1
- Update to RELEASE.2022-12-02T19-19-22Z

* Thu Dec 01 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221129T234049Z-1
- Update to RELEASE.2022-11-29T23-40-49Z

* Mon Nov 28 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221126T224332Z-1
- Update to RELEASE.2022-11-26T22-43-32Z

* Sat Nov 19 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221117T232009Z-1
- Update to RELEASE.2022-11-17T23-20-09Z

* Sat Nov 12 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221111T034420Z-1
- Update to RELEASE.2022-11-11T03-44-20Z

* Fri Nov 11 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221110T182021Z-1
- Update to RELEASE.2022-11-10T18-20-21Z

* Wed Nov 09 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221108T052707Z-1
- Update to RELEASE.2022-11-08T05-27-07Z

* Sun Oct 30 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221029T062133Z-1
- Update to RELEASE.2022-10-29T06-21-33Z

* Tue Oct 25 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221024T183507Z-1
- Update to RELEASE.2022-10-24T18-35-07Z

* Sun Oct 23 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221021T223748Z-1
- Update to RELEASE.2022-10-21T22-37-48Z

* Fri Oct 21 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221020T005509Z-1
- Update to RELEASE.2022-10-20T00-55-09Z

* Mon Oct 17 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221015T195703Z-1
- Update to RELEASE.2022-10-15T19-57-03Z

* Mon Oct 10 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221008T201100Z-1
- Update to RELEASE.2022-10-08T20-11-00Z

* Thu Oct 06 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221005T145827Z-1
- Update to RELEASE.2022-10-05T14-58-27Z

* Tue Oct 04 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221002T192929Z-1
- Update to RELEASE.2022-10-02T19-29-29Z

* Tue Sep 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220925T154453Z-1
- Update to RELEASE.2022-09-25T15-44-53Z

* Sat Sep 24 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220922T185727Z-1
- Update to RELEASE.2022-09-22T18-57-27Z

* Sun Sep 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220917T000945Z-1
- Update to RELEASE.2022-09-17T00-09-45Z

* Fri Sep 09 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220907T222502Z-1
- Update to RELEASE.2022-09-07T22-25-02Z

* Sat Sep 03 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220901T235336Z-1
- Update to RELEASE.2022-09-01T23-53-36Z

* Mon Aug 29 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220826T195315Z-1
- Update to RELEASE.2022-08-26T19-53-15Z

* Fri Aug 26 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220825T071705Z-1
- Update to RELEASE.2022-08-25T07-17-05Z

* Wed Aug 24 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220822T235306Z-1
- Update to RELEASE.2022-08-22T23-53-06Z

* Mon Aug 15 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220813T215444Z-1
- Update to RELEASE.2022-08-13T21-54-44Z

* Sat Aug 13 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220811T043728Z-1
- Update to RELEASE.2022-08-11T04-37-28Z

* Tue Aug 09 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220808T183409Z-1
- Update to RELEASE.2022-08-08T18-34-09Z

* Sat Aug 06 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220805T232709Z-1
- Update to RELEASE.2022-08-05T23-27-09Z

* Thu Aug 04 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220802T235916Z-1
- Update to RELEASE.2022-08-02T23-59-16Z

* Sun Jul 31 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220730T052140Z-1
- Update to RELEASE.2022-07-30T05-21-40Z

* Sat Jul 30 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220729T194048Z-1
- Update to RELEASE.2022-07-29T19-40-48Z

* Wed Jul 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220726T005303Z-1
- Update to RELEASE.2022-07-26T00-53-03Z

* Mon Jul 25 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220724T170931Z-1
- Update to RELEASE.2022-07-24T17-09-31Z

* Mon Jul 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220717T154314Z-1
- Update to RELEASE.2022-07-17T15-43-14Z

* Sat Jul 16 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220715T034422Z-1
- Update to RELEASE.2022-07-15T03-44-22Z

* Thu Jul 14 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220713T232944Z-1
- Update to RELEASE.2022-07-13T23-29-44Z

* Sat Jul 09 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220708T000523Z-1
- Update to RELEASE.2022-07-08T00-05-23Z

* Thu Jul 07 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220706T202949Z-1
- Update to RELEASE.2022-07-06T20-29-49Z

* Tue Jul 05 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220704T210254Z-1
- Update to RELEASE.2022-07-04T21-02-54Z

* Sat Jul 02 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220630T205809Z-1
- Update to RELEASE.2022-06-30T20-58-09Z

* Mon Jun 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220625T155016Z-1
- Update to RELEASE.2022-06-25T15-50-16Z

* Wed Jun 22 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220620T231345Z-1
- Update to RELEASE.2022-06-20T23-13-45Z

* Sat Jun 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220617T020035Z-1
- Update to RELEASE.2022-06-17T02-00-35Z

* Sun Jun 12 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220611T195532Z-1
- Update to RELEASE.2022-06-11T19-55-32Z

* Sat Jun 11 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220610T165915Z-1
- Update to RELEASE.2022-06-10T16-59-15Z

* Wed Jun 08 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220607T003341Z-1
- Update to RELEASE.2022-06-07T00-33-41Z

* Tue Jun 07 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220606T231452Z-1
- Update to RELEASE.2022-06-06T23-14-52Z

* Sat Jun 04 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220603T014053Z-1
- Update to RELEASE.2022-06-03T01-40-53Z

* Fri Jun 03 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220602T161626Z-1
- Update to RELEASE.2022-06-02T16-16-26Z

* Fri May 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220526T054841Z-1
- Update to RELEASE.2022-05-26T05-48-41Z

* Tue May 24 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220523T184511Z-1
- Update to RELEASE.2022-05-23T18-45-11Z

* Fri May 20 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220519T182059Z-1
- Update to RELEASE.2022-05-19T18-20-59Z

* Tue May 10 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220508T235031Z-1
- Update to RELEASE.2022-05-08T23-50-31Z

* Thu May 05 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220504T074527Z-1
- Update to RELEASE.2022-05-04T07-45-27Z

* Wed May 04 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220503T203608Z-1
- Update to RELEASE.2022-05-03T20-36-08Z

* Mon May 02 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220430T222353Z-1
- Update to RELEASE.2022-04-30T22-23-53Z

* Sat Apr 30 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220429T012709Z-1
- Update to RELEASE.2022-04-29T01-27-09Z

* Wed Apr 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220426T012024Z-1
- Update to RELEASE.2022-04-26T01-20-24Z

* Sun Apr 17 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220416T042602Z-1
- Update to RELEASE.2022-04-16T04-26-02Z

* Wed Apr 13 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220412T065535Z-1
- Update to RELEASE.2022-04-12T06-55-35Z

* Sun Apr 10 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220409T150952Z-1
- Update to RELEASE.2022-04-09T15-09-52Z

* Sat Apr 09 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220408T194435Z-1
- Update to RELEASE.2022-04-08T19-44-35Z

* Sat Apr 02 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220401T034139Z-1
- Update to RELEASE.2022-04-01T03-41-39Z

* Sun Mar 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220326T064928Z-1
- Update to RELEASE.2022-03-26T06-49-28Z

* Fri Mar 25 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220324T004344Z-1
- Update to RELEASE.2022-03-24T00-43-44Z

* Wed Mar 23 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220322T020510Z-1
- Update to RELEASE.2022-03-22T02-05-10Z

* Fri Mar 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220317T063449Z-1
- Update to RELEASE.2022-03-17T06-34-49Z

* Tue Mar 15 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220314T182524Z-1
- Update to RELEASE.2022-03-14T18-25-24Z

* Mon Mar 14 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220311T235745Z-1
- Update to RELEASE.2022-03-11T23-57-45Z

* Sat Mar 12 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220311T110823Z-1
- Update to RELEASE.2022-03-11T11-08-23Z

* Thu Mar 10 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220308T222851Z-1
- Update to RELEASE.2022-03-08T22-28-51Z

* Sun Mar 06 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220305T063239Z-1
- Update to RELEASE.2022-03-05T06-32-39Z

* Fri Mar 04 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220303T212116Z-1
- Update to RELEASE.2022-03-03T21-21-16Z

* Sun Feb 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220226T025446Z-1
- Update to RELEASE.2022-02-26T02-54-46Z

* Fri Feb 25 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220224T221201Z-1
- Update to RELEASE.2022-02-24T22-12-01Z

* Sat Feb 19 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220218T015010Z-1
- Update to RELEASE.2022-02-18T01-50-10Z

* Fri Feb 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220217T232226Z-1
- Update to RELEASE.2022-02-17T23-22-26Z

* Thu Feb 17 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220216T003527Z-1
- Update to RELEASE.2022-02-16T00-35-27Z

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
