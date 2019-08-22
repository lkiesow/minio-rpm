%define debug_package %{nil}

%define  tag   RELEASE.2019-08-21T19-40-07Z
%define  stag  RELEASE.20190821T194007Z
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
      useradd -M -r -u %{nuid} -d /srv/opencast -g %{gid} %{uid} > /dev/null 2>&1 || :
   else
      useradd -M -r -d /srv/opencast -g %{gid} %{uid} > /dev/null 2>&1 || :
   fi
fi


%post
%systemd_post opencast.service


%preun
%systemd_preun opencast.service


%postun
%systemd_postun_with_restart opencast.service


%files
%defattr(-,root,root,-)
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/minio
%{_unitdir}/minio.service
%attr(755,%{uid},%{gid}) %dir %{_sharedstatedir}/minio
%license LICENSE


%changelog
* Tue Aug 20 2019 Lars Kiesow <lkiesow@uos.de> 0.1.RELEASE.20190814T203741Z-1
- initial build
