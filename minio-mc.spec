%define debug_package %{nil}

%define  tag   RELEASE.2021-10-07T04-19-58Z
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
