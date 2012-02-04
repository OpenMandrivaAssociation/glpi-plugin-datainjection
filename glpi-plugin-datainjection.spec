%if %mandriva_branch == Cooker
%define release %mkrel 3
%else
%define subrel 1
%define release %mkrel 0
%endif

Summary: SNMP agent plugin
Name: glpi-plugin-datainjection
Version: 2.1.2
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/show/datainjection
Source0: https://forge.indepnet.net/attachments/download/1010/glpi-datainjection-%{version}.tar.gz
BuildArch: noarch
Provides: glpi-data-injection = %{version}-%{release}
Obsoletes: glpi-data-injection

%description
This plugin allows data import into GLPI using CSV files
It allows to create models of injection for a future re-use. It's been created
in order to :
- Import datas coming from others asset management softwares
- Inject electronic delivery forms
Datas to be imported using the plugains are :
- Inventory datas (except softwares and licenses)
- Management datas (contract, contact, supplier)
- Configuration datas (user, group, entity)

%prep

%setup -q -n datainjection

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/datainjection
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/datainjection
rm -rf %{buildroot}%{_datadir}/glpi/plugins/datainjection/docs

%files
%doc docs/*
%{_datadir}/glpi/plugins/datainjection
