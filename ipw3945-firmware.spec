#
%define		nameprog ipw3945

Summary:	Firmware for the Intel(R) PRO/Wireless 3945 Driver
Summary(pl.UTF-8):	Firmware dla sterownika do kart Intel(R) PRO/Wireless 3945
Name:		ipw3945-firmware
Version:	1.14.2
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://bughost.org/ipw3945/ucode/%{nameprog}-ucode-%{version}.tgz
# Source0-md5:	c1c4cc7f993f448e7c05768c012084aa
URL:		http://bughost.org/ipw3945/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the ipw-3945 driver. Usage of
the firmware is subject to the terms contained in
/lib/firmware/ipw3945-LICENSE. Please read the license carefully.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla sterownika ipw-3945. Można go używać
na warunkach zawartych w pliku /lib/firmware/ipw3945-LICENSE. Proszę
uważnie przeczytać licencję.

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
