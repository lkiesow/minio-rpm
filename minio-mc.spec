%define debug_package %{nil}

%define  tag   RELEASE.2025-07-21T05-28-08Z
%define  stag  %(echo "%{tag}" | tr -d '-')

Name:          minio-mc
Summary:       MinIO Client
Version:       0.1.%{stag}
Release:       1%{?dist}
License:       ASL 2.0

Source0:       https://dl.min.io/client/mc/release/linux-amd64/archive/mc.%{tag}
Source1:       https://raw.githubusercontent.com/minio/mc/%{tag}/LICENSE
URL:           https://min.io
BuildRoot:     %{_tmppath}/%{name}-root


%description
MinIO Client is a replacement for ls, cp, mkdir, diff and rsync commands for
filesystems and object storage.


%prep

%build

%install
rm -rf %{buildroot}

# install binary
install -p -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
cp %{SOURCE1} .


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%license LICENSE


%changelog
* Thu Jul 24 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250721T052808Z-1
- Update to RELEASE.2025-07-21T05-28-08Z

* Sat Jul 19 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250716T153503Z-1
- Update to RELEASE.2025-07-16T15-35-03Z

* Mon May 26 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250521T015954Z-1
- Update to RELEASE.2025-05-21T01-59-54Z

* Wed Apr 23 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250416T181326Z-1
- Update to RELEASE.2025-04-16T18-13-26Z

* Wed Apr 09 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250408T153949Z-1
- Update to RELEASE.2025-04-08T15-39-49Z

* Fri Apr 04 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250403T170756Z-1
- Update to RELEASE.2025-04-03T17-07-56Z

* Thu Mar 13 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250312T172924Z-1
- Update to RELEASE.2025-03-12T17-29-24Z

* Sat Mar 01 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250221T160046Z-1
- Update to RELEASE.2025-02-21T16-00-46Z

* Wed Feb 19 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250215T103616Z-1
- Update to RELEASE.2025-02-15T10-36-16Z

* Sun Feb 09 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250208T191421Z-1
- Update to RELEASE.2025-02-08T19-14-21Z

* Wed Feb 05 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250204T045750Z-1
- Update to RELEASE.2025-02-04T04-57-50Z

* Sun Jan 19 2025 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20250117T232550Z-1
- Update to RELEASE.2025-01-17T23-25-50Z

* Mon Dec 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241121T172154Z-1
- Update to RELEASE.2024-11-21T17-21-54Z

* Tue Nov 19 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241117T193525Z-1
- Update to RELEASE.2024-11-17T19-35-25Z

* Fri Nov 08 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241105T112945Z-1
- Update to RELEASE.2024-11-05T11-29-45Z

* Thu Oct 31 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241029T153459Z-1
- Update to RELEASE.2024-10-29T15-34-59Z

* Wed Oct 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241008T093726Z-1
- Update to RELEASE.2024-10-08T09-37-26Z

* Thu Oct 03 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20241002T082728Z-1
- Update to RELEASE.2024-10-02T08-27-28Z

* Tue Sep 17 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240916T174314Z-1
- Update to RELEASE.2024-09-16T17-43-14Z

* Wed Sep 11 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240909T075310Z-1
- Update to RELEASE.2024-09-09T07-53-10Z

* Tue Aug 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240826T104958Z-1
- Update to RELEASE.2024-08-26T10-49-58Z

* Sun Aug 18 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240817T113350Z-1
- Update to RELEASE.2024-08-17T11-33-50Z

* Wed Aug 14 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240813T053317Z-1
- Update to RELEASE.2024-08-13T05-33-17Z

* Sun Aug 04 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240731T155833Z-1
- Update to RELEASE.2024-07-31T15-58-33Z

* Sun Jul 28 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240726T130844Z-1
- Update to RELEASE.2024-07-26T13-08-44Z

* Wed Jul 24 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240722T200249Z-1
- Update to RELEASE.2024-07-22T20-02-49Z

* Tue Jul 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240715T174606Z-1
- Update to RELEASE.2024-07-15T17-46-06Z

* Sun Jul 14 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240711T180128Z-1
- Update to RELEASE.2024-07-11T18-01-28Z

* Tue Jul 09 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240708T205924Z-1
- Update to RELEASE.2024-07-08T20-59-24Z

* Fri Jul 05 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240703T201725Z-1
- Update to RELEASE.2024-07-03T20-17-25Z

* Sun Jun 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240629T190846Z-1
- Update to RELEASE.2024-06-29T19-08-46Z

* Thu Jun 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240624T194033Z-1
- Update to RELEASE.2024-06-24T19-40-33Z

* Sun Jun 23 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240620T145054Z-1
- Update to RELEASE.2024-06-20T14-50-54Z

* Sat Jun 15 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240612T143403Z-1
- Update to RELEASE.2024-06-12T14-34-03Z

* Wed Jun 12 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240610T164415Z-1
- Update to RELEASE.2024-06-10T16-44-15Z

* Fri Jun 07 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240605T181330Z-1
- Update to RELEASE.2024-06-05T18-13-30Z

* Wed Jun 05 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240601T150335Z-1
- Update to RELEASE.2024-06-01T15-03-35Z

* Tue May 28 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240524T090849Z-1
- Update to RELEASE.2024-05-24T09-08-49Z

* Sat May 11 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240509T170424Z-1
- Update to RELEASE.2024-05-09T17-04-24Z

* Wed May 08 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240503T112107Z-1
- Update to RELEASE.2024-05-03T11-21-07Z

* Tue Apr 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240429T095605Z-1
- Update to RELEASE.2024-04-29T09-56-05Z

* Fri Apr 19 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240418T164529Z-1
- Update to RELEASE.2024-04-18T16-45-29Z

* Sun Mar 31 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240330T152952Z-1
- Update to RELEASE.2024-03-30T15-29-52Z

* Wed Mar 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240325T164114Z-1
- Update to RELEASE.2024-03-25T16-41-14Z

* Sat Mar 23 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240320T210729Z-1
- Update to RELEASE.2024-03-20T21-07-29Z

* Sat Mar 16 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240313T235157Z-1
- Update to RELEASE.2024-03-13T23-51-57Z

* Mon Mar 11 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240309T064306Z-1
- Update to RELEASE.2024-03-09T06-43-06Z

* Fri Mar 08 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240307T003149Z-1
- Update to RELEASE.2024-03-07T00-31-49Z

* Mon Mar 04 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240303T001308Z-1
- Update to RELEASE.2024-03-03T00-13-08Z

* Mon Feb 26 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240224T013320Z-1
- Update to RELEASE.2024-02-24T01-33-20Z

* Sun Feb 18 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240216T110548Z-1
- Update to RELEASE.2024-02-16T11-05-48Z

* Thu Feb 15 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240214T211952Z-1
- Update to RELEASE.2024-02-14T21-19-52Z

* Sat Feb 10 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240209T221824Z-1
- Update to RELEASE.2024-02-09T22-18-24Z

* Thu Feb 01 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240131T085940Z-1
- Update to RELEASE.2024-01-31T08-59-40Z

* Tue Jan 30 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240128T162314Z-1
- Update to RELEASE.2024-01-28T16-23-14Z

* Sat Jan 20 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240118T070339Z-1
- Update to RELEASE.2024-01-18T07-03-39Z

* Wed Jan 17 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240116T160634Z-1
- Update to RELEASE.2024-01-16T16-06-34Z

* Sun Jan 14 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240113T084448Z-1
- Update to RELEASE.2024-01-13T08-44-48Z

* Fri Jan 12 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240111T054932Z-1
- Update to RELEASE.2024-01-11T05-49-32Z

* Sun Jan 07 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20240105T050432Z-1
- Update to RELEASE.2024-01-05T05-04-32Z

* Tue Jan 02 2024 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231229T201529Z-1
- Update to RELEASE.2023-12-29T20-15-29Z

* Sun Dec 24 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231223T084721Z-1
- Update to RELEASE.2023-12-23T08-47-21Z

* Thu Dec 21 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231220T071422Z-1
- Update to RELEASE.2023-12-20T07-14-22Z

* Fri Dec 15 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231214T003741Z-1
- Update to RELEASE.2023-12-14T00-37-41Z

* Sun Dec 10 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231207T221317Z-1
- Update to RELEASE.2023-12-07T22-13-17Z

* Thu Dec 07 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231202T112410Z-1
- Update to RELEASE.2023-12-02T11-24-10Z

* Sun Dec 03 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231202T020328Z-1
- Update to RELEASE.2023-12-02T02-03-28Z

* Tue Nov 21 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231120T163059Z-1
- Update to RELEASE.2023-11-20T16-30-59Z

* Fri Nov 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231115T224558Z-1
- Update to RELEASE.2023-11-15T22-45-58Z

* Sun Nov 12 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231110T213717Z-1
- Update to RELEASE.2023-11-10T21-37-17Z

* Thu Nov 09 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231106T041923Z-1
- Update to RELEASE.2023-11-06T04-19-23Z

* Thu Nov 02 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231030T184332Z-1
- Update to RELEASE.2023-10-30T18-43-32Z

* Thu Oct 26 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231024T214222Z-1
- Update to RELEASE.2023-10-24T21-42-22Z

* Wed Oct 25 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231024T051828Z-1
- Update to RELEASE.2023-10-24T05-18-28Z

* Sun Oct 15 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231014T015703Z-1
- Update to RELEASE.2023-10-14T01-57-03Z

* Mon Oct 09 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20231004T065256Z-1
- Update to RELEASE.2023-10-04T06-52-56Z

* Sun Oct 01 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230929T164122Z-1
- Update to RELEASE.2023-09-29T16-41-22Z

* Fri Sep 29 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230928T174830Z-1
- Update to RELEASE.2023-09-28T17-48-30Z

* Tue Sep 26 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230922T050746Z-1
- Update to RELEASE.2023-09-22T05-07-46Z

* Fri Sep 22 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230920T152231Z-1
- Update to RELEASE.2023-09-20T15-22-31Z

* Sun Sep 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230913T230858Z-1
- Update to RELEASE.2023-09-13T23-08-58Z

* Fri Sep 08 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230907T224855Z-1
- Update to RELEASE.2023-09-07T22-48-55Z

* Tue Sep 05 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230902T212803Z-1
- Update to RELEASE.2023-09-02T21-28-03Z

* Sat Sep 02 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230830T080226Z-1
- Update to RELEASE.2023-08-30T08-02-26Z

* Thu Aug 31 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230829T225506Z-1
- Update to RELEASE.2023-08-29T22-55-06Z

* Fri Aug 25 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230818T215755Z-1
- Update to RELEASE.2023-08-18T21-57-55Z

* Thu Aug 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230815T230309Z-1
- Update to RELEASE.2023-08-15T23-03-09Z

* Thu Aug 10 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230808T172359Z-1
- Update to RELEASE.2023-08-08T17-23-59Z

* Sat Aug 05 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230801T233057Z-1
- Update to RELEASE.2023-08-01T23-30-57Z

* Sat Jul 22 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230721T204427Z-1
- Update to RELEASE.2023-07-21T20-44-27Z

* Wed Jul 19 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230718T210538Z-1
- Update to RELEASE.2023-07-18T21-05-38Z

* Wed Jul 12 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230711T233044Z-1
- Update to RELEASE.2023-07-11T23-30-44Z

* Sat Jul 08 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230707T052551Z-1
- Update to RELEASE.2023-07-07T05-25-51Z

* Fri Jun 30 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230628T215417Z-1
- Update to RELEASE.2023-06-28T21-54-17Z

* Sun Jun 25 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230623T181207Z-1
- Update to RELEASE.2023-06-23T18-12-07Z

* Tue Jun 20 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230619T193119Z-1
- Update to RELEASE.2023-06-19T19-31-19Z

* Sat Jun 17 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230615T150826Z-1
- Update to RELEASE.2023-06-15T15-08-26Z

* Sun Jun 11 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230606T134856Z-1
- Update to RELEASE.2023-06-06T13-48-56Z

* Sun Jun 04 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230530T224138Z-1
- Update to RELEASE.2023-05-30T22-41-38Z

* Mon May 29 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230526T233154Z-1
- Update to RELEASE.2023-05-26T23-31-54Z

* Fri May 19 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230518T165900Z-1
- Update to RELEASE.2023-05-18T16-59-00Z

* Sat May 06 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230504T181016Z-1
- Update to RELEASE.2023-05-04T18-10-16Z

* Fri Apr 14 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230412T022151Z-1
- Update to RELEASE.2023-04-12T02-21-51Z

* Sat Apr 08 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230406T165110Z-1
- Update to RELEASE.2023-04-06T16-51-10Z

* Sat Mar 25 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230323T200304Z-1
- Update to RELEASE.2023-03-23T20-03-04Z

* Tue Mar 21 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230320T171753Z-1
- Update to RELEASE.2023-03-20T17-17-53Z

* Tue Feb 28 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230228T001259Z-1
- Update to RELEASE.2023-02-28T00-12-59Z

* Sat Feb 18 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230216T192011Z-1
- Update to RELEASE.2023-02-16T19-20-11Z

* Wed Feb 01 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230128T202938Z-1
- Update to RELEASE.2023-01-28T20-29-38Z

* Fri Jan 13 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20230111T031416Z-1
- Update to RELEASE.2023-01-11T03-14-16Z

* Wed Jan 04 2023 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221224T152138Z-1
- Update to RELEASE.2022-12-24T15-21-38Z

* Wed Dec 14 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221213T002328Z-1
- Update to RELEASE.2022-12-13T00-23-28Z

* Sat Dec 03 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221202T234847Z-1
- Update to RELEASE.2022-12-02T23-48-47Z

* Sat Nov 19 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221117T212039Z-1
- Update to RELEASE.2022-11-17T21-20-39Z

* Wed Nov 09 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221107T234739Z-1
- Update to RELEASE.2022-11-07T23-47-39Z

* Sun Oct 30 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221029T100923Z-1
- Update to RELEASE.2022-10-29T10-09-23Z

* Tue Oct 25 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221022T033929Z-1
- Update to RELEASE.2022-10-22T03-39-29Z

* Sat Oct 22 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221020T232633Z-1
- Update to RELEASE.2022-10-20T23-26-33Z

* Mon Oct 17 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221012T181250Z-1
- Update to RELEASE.2022-10-12T18-12-50Z

* Mon Oct 10 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221009T211059Z-1
- Update to RELEASE.2022-10-09T21-10-59Z

* Fri Oct 07 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221006T012006Z-1
- Update to RELEASE.2022-10-06T01-20-06Z

* Tue Oct 04 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20221001T075614Z-1
- Update to RELEASE.2022-10-01T07-56-14Z

* Sun Sep 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220916T091647Z-1
- Update to RELEASE.2022-09-16T09-16-47Z

* Tue Aug 30 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220828T200811Z-1
- Update to RELEASE.2022-08-28T20-08-11Z

* Wed Aug 24 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220823T054520Z-1
- Update to RELEASE.2022-08-23T05-45-20Z

* Sat Aug 13 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220811T003048Z-1
- Update to RELEASE.2022-08-11T00-30-48Z

* Sun Aug 07 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220805T080128Z-1
- Update to RELEASE.2022-08-05T08-01-28Z

* Sat Jul 30 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220729T191716Z-1
- Update to RELEASE.2022-07-29T19-17-16Z

* Mon Jul 25 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220724T022513Z-1
- Update to RELEASE.2022-07-24T02-25-13Z

* Tue Jul 19 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220715T092055Z-1
- Update to RELEASE.2022-07-15T09-20-55Z

* Fri Jul 15 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220711T161612Z-1
- Update to RELEASE.2022-07-11T16-16-12Z

* Thu Jul 07 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220706T145436Z-1
- Update to RELEASE.2022-07-06T14-54-36Z

* Mon Jun 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220626T185148Z-1
- Update to RELEASE.2022-06-26T18-51-48Z

* Sat Jun 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220617T025250Z-1
- Update to RELEASE.2022-06-17T02-52-50Z

* Wed Jun 15 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220611T211036Z-1
- Update to RELEASE.2022-06-11T21-10-36Z

* Sat Jun 11 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220610T222912Z-1
- Update to RELEASE.2022-06-10T22-29-12Z

* Tue May 10 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220509T040826Z-1
- Update to RELEASE.2022-05-09T04-08-26Z

* Thu May 05 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220504T060755Z-1
- Update to RELEASE.2022-05-04T06-07-55Z

* Wed Apr 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220426T180022Z-1
- Update to RELEASE.2022-04-26T18-00-22Z

* Sun Apr 17 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220416T211121Z-1
- Update to RELEASE.2022-04-16T21-11-21Z

* Fri Apr 08 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220407T214327Z-1
- Update to RELEASE.2022-04-07T21-43-27Z

* Sat Apr 02 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220401T234448Z-1
- Update to RELEASE.2022-04-01T23-44-48Z

* Fri Apr 01 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220331T045530Z-1
- Update to RELEASE.2022-03-31T04-55-30Z

* Fri Mar 18 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220317T202506Z-1
- Update to RELEASE.2022-03-17T20-25-06Z

* Mon Mar 14 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220313T223400Z-1
- Update to RELEASE.2022-03-13T22-34-00Z

* Thu Mar 10 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220309T020836Z-1
- Update to RELEASE.2022-03-09T02-08-36Z

* Fri Mar 04 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220303T211224Z-1
- Update to RELEASE.2022-03-03T21-12-24Z

* Sun Feb 27 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220226T035831Z-1
- Update to RELEASE.2022-02-26T03-58-31Z

* Thu Feb 24 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220223T031559Z-1
- Update to RELEASE.2022-02-23T03-15-59Z

* Thu Feb 17 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220216T055401Z-1
- Update to RELEASE.2022-02-16T05-54-01Z

* Tue Feb 08 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220207T092534Z-1
- Update to RELEASE.2022-02-07T09-25-34Z

* Thu Feb 03 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220202T020324Z-1
- Update to RELEASE.2022-02-02T02-03-24Z

* Sun Jan 30 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220129T010327Z-1
- Update to RELEASE.2022-01-29T01-03-27Z

* Wed Jan 26 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220125T210201Z-1
- Update to RELEASE.2022-01-25T21-02-01Z

* Sat Jan 08 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220107T060138Z-1
- Update to RELEASE.2022-01-07T06-01-38Z

* Fri Jan 07 2022 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20220105T235251Z-1
- Update to RELEASE.2022-01-05T23-52-51Z

* Thu Dec 30 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211229T065255Z-1
- Update to RELEASE.2021-12-29T06-52-55Z

* Tue Dec 21 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211220T234334Z-1
- Update to RELEASE.2021-12-20T23-43-34Z

* Fri Dec 17 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211216T233839Z-1
- Update to RELEASE.2021-12-16T23-38-39Z

* Sat Dec 11 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211210T001428Z-1
- Update to RELEASE.2021-12-10T00-14-28Z

* Wed Nov 17 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211116T203736Z-1
- Update to RELEASE.2021-11-16T20-37-36Z

* Sat Nov 06 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211105T100506Z-1
- Update to RELEASE.2021-11-05T10-05-06Z

* Fri Oct 08 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20211007T041958Z-1
- Update to RELEASE.2021-10-07T04-19-58Z

* Fri Sep 24 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210923T054403Z-1
- Update to RELEASE.2021-09-23T05-44-03Z

* Wed Sep 08 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210902T092127Z-1
- Update to RELEASE.2021-09-02T09-21-27Z

* Wed Jul 28 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210727T064619Z-1
- Update to RELEASE.2021-07-27T06-46-19Z

* Mon Jun 14 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210613T174822Z-1
- Update to RELEASE.2021-06-13T17-48-22Z

* Wed Jun 09 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210608T012937Z-1
- Update to RELEASE.2021-06-08T01-29-37Z

* Thu May 27 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210526T191926Z-1
- Update to RELEASE.2021-05-26T19-19-26Z

* Wed May 19 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210518T033944Z-1
- Update to RELEASE.2021-05-18T03-39-44Z

* Thu May 13 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210512T031011Z-1
- Update to RELEASE.2021-05-12T03-10-11Z

* Fri Apr 23 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210422T174000Z-1
- Update to RELEASE.2021-04-22T17-40-00Z

* Wed Mar 24 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210323T054611Z-1
- Update to RELEASE.2021-03-23T05-46-11Z

* Sat Mar 13 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210312T033659Z-1
- Update to RELEASE.2021-03-12T03-36-59Z

* Thu Mar 11 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210310T055920Z-1
- Update to RELEASE.2021-03-10T05-59-20Z

* Sun Mar 07 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210306T221644Z-1
- Update to RELEASE.2021-03-06T22-16-44Z

* Sat Feb 20 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210219T053440Z-1
- Update to RELEASE.2021-02-19T05-34-40Z

* Mon Feb 15 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210214T042806Z-1
- Update to RELEASE.2021-02-14T04-28-06Z

* Thu Feb 11 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210210T073257Z-1
- Update to RELEASE.2021-02-10T07-32-57Z

* Mon Feb 08 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210207T020205Z-1
- Update to RELEASE.2021-02-07T02-02-05Z

* Sun Jan 31 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210130T005042Z-1
- Update to RELEASE.2021-01-30T00-50-42Z

* Sun Jan 17 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210116T024534Z-1
- Update to RELEASE.2021-01-16T02-45-34Z

* Wed Jan 06 2021 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20210105T050358Z-1
- Update to RELEASE.2021-01-05T05-03-58Z

* Sat Dec 19 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201218T105353Z-1
- Update to RELEASE.2020-12-18T10-53-53Z

* Fri Dec 11 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201210T012617Z-1
- Update to RELEASE.2020-12-10T01-26-17Z

* Thu Nov 26 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201125T230407Z-1
- Update to RELEASE.2020-11-25T23-04-07Z

* Wed Nov 18 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201117T003914Z-1
- Update to RELEASE.2020-11-17T00-39-14Z

* Sun Oct 04 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20201003T025456Z-1
- Update to RELEASE.2020-10-03T02-54-56Z

* Thu Sep 24 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200923T200213Z-1
- Update to RELEASE.2020-09-23T20-02-13Z

* Sat Sep 19 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200918T001321Z-1
- Update to RELEASE.2020-09-18T00-13-21Z

* Fri Sep 04 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200903T000828Z-1
- Update to RELEASE.2020-09-03T00-08-28Z

* Fri Aug 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200820T002301Z-1
- Update to RELEASE.2020-08-20T00-23-01Z

* Sun Aug 09 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200808T023358Z-1
- Update to RELEASE.2020-08-08T02-33-58Z

* Sun Aug 02 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200731T233413Z-1
- Update to RELEASE.2020-07-31T23-34-13Z

* Sat Jul 18 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200717T025220Z-1
- Update to RELEASE.2020-07-17T02-52-20Z

* Sun Jul 12 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200711T051852Z-1
- Update to RELEASE.2020-07-11T05-18-52Z

* Sat Jun 27 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200626T195655Z-1
- Update to RELEASE.2020-06-26T19-56-55Z

* Sun Jun 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200620T001843Z-1
- Update to RELEASE.2020-06-20T00-18-43Z

* Wed Jun 17 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200616T192441Z-1
- Update to RELEASE.2020-06-16T19-24-41Z

* Sat May 30 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200528T234336Z-1
- Update to RELEASE.2020-05-28T23-43-36Z

* Sun May 17 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200516T014437Z-1
- Update to RELEASE.2020-05-16T01-44-37Z

* Fri May 08 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200506T180007Z-1
- Update to RELEASE.2020-05-06T18-00-07Z

* Wed May 06 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200505T060347Z-1
- Update to RELEASE.2020-05-05T06-03-47Z

* Sun Apr 26 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200425T004323Z-1
- Update to RELEASE.2020-04-25T00-43-23Z

* Tue Apr 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200419T191753Z-1
- Update to RELEASE.2020-04-19T19-17-53Z

* Sat Apr 18 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200417T085548Z-1
- Update to RELEASE.2020-04-17T08-55-48Z

* Thu Apr 16 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200415T201800Z-1
- Update to RELEASE.2020-04-15T20-18-00Z

* Tue Apr 07 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200404T052855Z-1
- Update to RELEASE.2020-04-04T05-28-55Z

* Fri Apr 03 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200402T215012Z-1
- Update to RELEASE.2020-04-02T21-50-12Z

* Sun Mar 15 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200314T012337Z-1
- Update to RELEASE.2020-03-14T01-23-37Z

* Sat Mar 07 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200306T232945Z-1
- Update to RELEASE.2020-03-06T23-29-45Z

* Fri Feb 28 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200225T181003Z-1
- Update to RELEASE.2020-02-25T18-10-03Z

* Fri Feb 21 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200220T234954Z-1
- Update to RELEASE.2020-02-20T23-49-54Z

* Sat Feb 15 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200214T193550Z-1
- Update to RELEASE.2020-02-14T19-35-50Z

* Thu Feb 06 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200205T200722Z-1
- Update to RELEASE.2020-02-05T20-07-22Z

* Mon Jan 27 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200125T030219Z-1
- Update to RELEASE.2020-01-25T03-02-19Z

* Tue Jan 14 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200113T224903Z-1
- Update to RELEASE.2020-01-13T22-49-03Z

* Sun Jan 05 2020 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20200103T203314Z-1
- Update to RELEASE.2020-01-03T20-33-14Z

* Thu Dec 26 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191224T234136Z-1
- Update to RELEASE.2019-12-24T23-41-36Z

* Wed Dec 18 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191217T232628Z-1
- Update to RELEASE.2019-12-17T23-26-28Z

* Fri Oct 11 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191009T225457Z-1
- Update to RELEASE.2019-10-09T22-54-57Z

* Fri Oct 04 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20191002T194102Z-1
- Update to RELEASE.2019-10-02T19-41-02Z

* Sun Sep 22 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20190920T000955Z-1
- Update to RELEASE.2019-09-20T00-09-55Z

* Sun Sep 08 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20190905T234350Z-1
- Update to RELEASE.2019-09-05T23-43-50Z

* Sun Aug 25 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.-1
- Update to RELEASE.2019-08-21T19-59-10Z
- Generate stag via macro

* Thu Aug 22 2019 Lars Kiesow <lkiesow@uos.de> - 0.1.RELEASE.20190814T204949Z-1
- Update to RELEASE.2019-08-14T20-49-49Z

* Wed Aug 21 2019 Lars Kiesow <lkiesow@uos.de> 0.1.RELEASE.20190814T204949Z-1
- initial build
