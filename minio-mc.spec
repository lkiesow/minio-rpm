%define debug_package %{nil}

%define  tag   RELEASE.2019-10-02T19-41-02Z
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
