Name:           oolandlock
Version:        0.1.0
Release:        1%{?dist}
Summary:        Enforces unprivileged filesystem sandboxing via the Linux Landlock LSM.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oolandlock
Source0:        oolandlock-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oolandlock is a sovereign, capability-bounded LANDLOCK LSM written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oolandlock
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oolandlock-uninstall

%files
/usr/bin/oolandlock
/usr/bin/oolandlock-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
