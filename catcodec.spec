Name:           catcodec
Version:        1.0.1
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
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc bundle/*.txt
%{_bindir}/*
%{_mandir}/man1/%{name}*
