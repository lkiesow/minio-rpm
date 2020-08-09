%define debug_package %{nil}

%define  tag   RELEASE.2020-08-08T02-33-58Z
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
