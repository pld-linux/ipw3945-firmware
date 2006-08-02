#
%define		nameprog ipw3945

Summary:	Firmware for the Intel(R) PRO/Wireless 3945 Driver
Summary(pl):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 3945
Name:		ipw3945-firmware
Version:	1.13
Release:	0.1
License:	distributable
Group:		System Environment/Kernel
Source0:	http://bughost.org/%{nameprog}/ucode/%{nameprog}-ucode-%{version}.tgz
# Source0-md5:	9190f498f85f83135ee7e7a1d330832e
URL:		http://ipw3945.sourceforge.net/firmware.php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the ipw-3945 driver. Usage of
the firmware is subject to the terms contained in
/lib/firmware/ipw3945-LICENSE. Please read the license carefully.

%description -l pl
Ten pakiet zawiera firmware dla sterownika ipw-3945. Mo¿na go u¿ywaæ
na warunkach zawartych w pliku /lib/firmware/ipw3945-LICENSE. Proszê
uwa¿nie przeczytaæ licencjê.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install -p %{nameprog}-ucode-%{version}/*.ucode $RPM_BUILD_ROOT/lib/firmware
install -p %{nameprog}-ucode-%{version}/LICENSE.%{nameprog}-ucode $RPM_BUILD_ROOT/lib/firmware/%{nameprog}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/%{nameprog}-LICENSE
/lib/firmware/*.ucode
