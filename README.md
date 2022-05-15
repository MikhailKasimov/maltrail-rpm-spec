# maltrail-rpm-spec
Maltrail RPM-package spec-file.

This file allows to build installation-ready [Maltrail](https://github.com/stamparm/maltrail) malicious traffic detection system package for various RPM-based Linux distros.

- Currently sucessfully works for:
```
CentOS 7
CentOS 8
CentOS 8 Stream
Fedora 27
Fedora 28
Fedora 29
Fedora 30
Fedora 31
Fedora 32
Fedora 33
Fedora 34
Fedora 35
Fedora 36
Fedora Rawhide
Mageia 7
Mageia 8
Mageia Cauldron
SUSE Linux Enterprise 15 SP2
SUSE Linux Enterprise 15 SP3
ScientificLinux 7
openEuler 20.03
openEuler 21.03
openSUSE Factory ARM
openSUSE Factory PowerPC
openSUSE Factory RISCV
openSUSE Factory zSystems
openSUSE Leap 15.2
openSUSE Leap 15.2 ARM
openSUSE Leap 15.2 PowerPC
openSUSE Leap 15.3
openSUSE Leap 15.4
openSUSE Tumbleweed
```

- Built for archs: i586/x86_64/armv7l/aarch64/ppc64(-le)/s390x/riscv64

- Built by openSUSE Open Build System (OBS): https://build.opensuse.org/

- OBS repo: https://build.opensuse.org/package/show/home:k_mikhail/maltrail

- Installation page: https://software.opensuse.org/package/maltrail

## Known issues

On Maltrail package uninstallation system returns message:
```
rm: cannot remove '/var/lib/systemd/migrated/maltrail-sensor': No such file or directory
rm: cannot remove '/var/lib/systemd/migrated/maltrail-server': No such file or directory
rm: cannot remove '/var/lib/systemd/migrated/maltrail-ips': No such file or directory
rm: cannot remove '/var/lib/systemd/migrated/maltrail-ips': No such file or directory
```
but package anyway gets uninstalled correctly. Currently this message can be ignored.

Reason is job of ```%pre```, ```%post```, ```%preun```, ```%postun``` macros for systemd services of Maltrail components. 

## License

This software is provided under a MIT License as the original [Maltrail project](https://github.com/stamparm/maltrail/blob/master/README.md#license). See the accompanying [LICENSE](https://github.com/stamparm/maltrail/blob/master/LICENSE) file for more information.

## Links:

[Maltrail Project](https://github.com/stamparm/maltrail)

[Maltrail Wiki](https://github.com/stamparm/maltrail/wiki)

[Maltrail's systemd-based realization for IPS-mechanism](https://github.com/MikhailKasimov/systemd-based-maltrail-ips-mechanism)
