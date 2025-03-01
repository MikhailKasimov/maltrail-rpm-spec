#
# spec file for package maltrail
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           maltrail
Version:        0.79
Release:        0
Summary:        Malicious Traffic Detection System
Group:          Productivity/Security
License:        MIT
URL:            https://github.com/stamparm/maltrail
#URL:           https://github.com/MikhailKasimov/systemd-based-maltrail-ips-mechanism
Source0:        https://github.com/stamparm/maltrail/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-ips.sh
Source2:        %{name}-ips.service
Source3:        %{name}-ips.timer
BuildRequires:  tar
BuildRequires:  python3-rpm-generators
%{?python_enable_dependency_generator}
Requires:       procps
Requires:       schedtool
Requires:       python-pcapy-ng
BuildArchitectures:    noarch
%{?systemd_requires}

%description
Maltrail is a malicious traffic detection system, utilizing
publicly available (black)lists containing malicious and/or
generally suspicious trails, along with static trails compiled
from various AV reports and custom user defined lists, where trail
can be anything from domain name (e.g. zvpprsensinaix.com for
Banjori malware), URL (e.g. hXXp://109.162.38.120/harsh02.exe for
known malicious executable), IP address (e.g. 185.130.5.231 for
known attacker) or HTTP User-Agent header value (e.g. sqlmap for
automatic SQL injection and database takeover tool). Also, it uses
(optional) advanced heuristic mechanisms that can help in
discovery of unknown threats (e.g. new malware).

%prep
%setup -q

%build
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done
cat << EOF > %{name}-sensor
python3 /opt/%{name}/sensor.py
EOF
sed -i '1 i #!/bin/bash\n' %{name}-sensor

cat << EOF > %{name}-server
python3 /opt/%{name}/server.py
EOF
sed -i '1 i #!/bin/bash\n' %{name}-server

%install
mkdir -p %{buildroot}%{_bindir} \
   %{buildroot}%{_unitdir} \
   %{buildroot}/%{_sbindir}/%{name}-sensor \
   %{buildroot}/%{_sbindir}/%{name}-server \
   %{buildroot}/%{_sbindir}/%{name}-ips
install -m 0755 -t %{buildroot}%{_bindir} %{name}-sensor
install -m 0755 -t %{buildroot}%{_bindir} %{name}-server
install -Dm 0644 -t %{buildroot}%{_unitdir} %{name}-sensor.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}-sensor
install -Dm 0644 -t %{buildroot}%{_unitdir} %{name}-server.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}-server
install -Dm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-ips.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}-ips
install -Dm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-ips.timer

mkdir -p %{buildroot}/opt/%{name}
cp -vr * %{buildroot}/opt/%{name}
sed -i -e 's/^M$//' %{SOURCE1}
cp -vr %{SOURCE1} %{buildroot}/opt/%{name}
chmod +x %{buildroot}/opt/%{name}/%{name}-ips.sh

%pre
%service_add_pre %{name}-sensor.service
%service_add_pre %{name}-server.service
%service_add_pre %{name}-ips.service
%service_add_pre %{name}-ips.timer

%post
%service_add_post %{name}-sensor.service
%service_add_post %{name}-server.service
%service_add_post %{name}-ips.service
%service_add_post %{name}-ips.timer

%preun
%service_del_preun %{name}-sensor.service
%service_del_preun %{name}-server.service
%service_del_preun %{name}-ips.service
%service_del_preun %{name}-ips.timer

%postun
%service_del_postun %{name}-sensor.service
%service_del_postun %{name}-server.service
%service_del_postun %{name}-ips.service
%service_del_postun %{name}-ips.timer

%files
%license LICENSE
%doc  CHANGELOG README.md
/opt/%{name}
/opt/%{name}/%{name}-ips.sh
%{_bindir}/%{name}-sensor
%{_bindir}/%{name}-server
%{_sbindir}/rc%{name}-sensor
%{_sbindir}/rc%{name}-server
%{_sbindir}/rc%{name}-ips
%{_unitdir}/%{name}-sensor.service
%{_unitdir}/%{name}-server.service
%{_unitdir}/%{name}-ips.service
%{_unitdir}/%{name}-ips.timer

%changelog
* Sat Mar 01 2025 - mikhail.kasimov@gmail.com
  - Version 0.79 (release)

  * Sat Feb 01 2025 - mikhail.kasimov@gmail.com
  - Version 0.78 (release)
  
* Wed Jan 01 2025 - mikhail.kasimov@gmail.com
  - Version 0.77 (release)
  
* Sun Dec 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.76 (release)

* Fri Nov 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.75 (release)

* Tue Oct 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.74 (release)

* Sun Sep 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.73 (release)
  
* Thu Aug 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.72 (release)
  
* Mon Jul 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.71 (release)

* Sat Jun 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.70 (release)
  
* Thu May 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.69 (release)
  
* Mon Apr 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.68 (release)
  
* Fri Mar 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.67 (release)
  
* Thu Feb 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.66 (release)
  
* Mon Jan 01 2024 - mikhail.kasimov@gmail.com
  - Version 0.65 (release)
  
* Fri Dec 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.64 (release)

* Wed Nov 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.63 (release)

* Sun Oct 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.62 (release)
  
* Fri Sep 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.61 (release)
  
* Tue Aug 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.60 (release)

* Thu Jul 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.59 (release)
  
* Thu Jun 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.58 (release)
  
* Mon May 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.57 (release)
  
* Sat Apr 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.56 (release)
  
* Wed Mar 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.55 (release)

* Wed Feb 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.54 (release)
  
* Sun Jan 01 2023 - mikhail.kasimov@gmail.com
  - Version 0.53 (release)

* Fri Dec 02 2022 - mikhail.kasimov@gmail.com
  - Version 0.52 (release)
  
* Tue Nov 01 2022 - mikhail.kasimov@gmail.com
  - Version 0.51 (release)

* Sun Oct 02 2022 - mikhail.kasimov@gmail.com
  - Version 0.50 (release)

* Fri Sep 02 2022 - mikhail.kasimov@gmail.com
  - Version 0.49 (release)

* Fri Aug 05 2022 - mikhail.kasimov@gmail.com
  - Version 0.48 (release)
  
* Wed Jul 01 2022 - mikhail.kasimov@gmail.com
  - Version 0.47 (release)
  
* Wed Jun 01 2022 - mikhail.kasimov@gmail.com
  - Version 0.46 (release)

* Tue May 03 2022 - mikhail.kasimov@gmail.com
  - Version 0.45 (release)
