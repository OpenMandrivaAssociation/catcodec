Name:           catcodec
Version:        1.0.2
Release:        %mkrel 1
Summary:        Sample catalog decoder and encoder for OpenTTD
Group:          Development/Other
License:        GPLv2+
URL:            http://www.openttd.org/en/download-catcodec
Source0:        http://binaries.openttd.org/extra/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Patch0:		catcodec-1.0.2-fix_linking_order.patch 
Patch1:		catcodec-1.0.2-add_Makefile.local.patch 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
catcodec decodes and encodes sample catalogs for OpenTTD. These sample
catalogs are not much more than some meta-data (description and file name)
and raw PCM data.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
cat << EOF >> Makefile.local
VERBOSE=1
CXXFLAGS=%{optflags}
LDFLAGS=%{ldflags}
prefix=%{_prefix}
DO_NOT_INSTALL_DOCS=1
DO_NOT_INSTALL_LICENSE=1
DO_NOT_INSTALL_CHANGELOG=1
EOF

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/readme.txt
%{_bindir}/*
%{_mandir}/man1/%{name}*
