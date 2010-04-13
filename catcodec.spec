Name:           catcodec
Version:        1.0.0
Release:        %mkrel 1
Summary:        Sample catalog decoder and encoder for OpenTTD
Group:          Development/Other
License:        GPLv2+
URL:            http://www.openttd.org/en/download-catcodec
Source0:        http://binaries.openttd.org/extra/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
catcodec decodes and encodes sample catalogs for OpenTTD. These sample
catalogs are not much more than some meta-data (description and file name)
and raw PCM data.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

# binary
install -D -m 755 catcodec %{buildroot}%{_bindir}/catcodec

# man page
install -D -m 755 catcodec.1 %{buildroot}%{_mandir}/man1/catcodec.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/*
%{_mandir}/man1/%{name}*
