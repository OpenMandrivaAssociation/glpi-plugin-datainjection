%define name glpi-plugin-datainjection
%define version 2.1.2
%define release %mkrel 1

Summary: SNMP agent plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/show/datainjection
Source0: https://forge.indepnet.net/attachments/download/1010/glpi-datainjection-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

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

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/datainjection
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/datainjection

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/glpi/plugins/datainjection
