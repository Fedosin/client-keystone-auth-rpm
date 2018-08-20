Name: client-keystone-auth
Version: OVERRIDE_THIS
Release: 00
License: ASL 2.0
Summary: Keystone client authentication for client-go

URL: https://k8s.io/cloud-provider-openstack"

Source0: client-keystone-auth

%description
Command-line utility for obtaining tokens from Keystone.

%install

install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -T %{SOURCE0} $RPM_BUILD_ROOT/usr/bin/client-keystone-auth

%files
%{_bindir}/client-keystone-auth
