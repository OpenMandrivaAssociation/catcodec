Name:		catcodec
Version:	1.0.5
Release:	4
Summary:	Sample catalog decoder and encoder for OpenTTD
Group:		Development/Other
License:	GPLv2+
URL:		http://www.openttd.org/en/download-catcodec
Source0:	http://binaries.openttd.org/extra/%{name}/%{version}/%{name}-%{version}-source.tar.xz
Patch0:		catcodec-1.0.2-fix_linking_order.patch

%description
catcodec decodes and encodes sample catalogs for OpenTTD. These sample
catalogs are not much more than some meta-data (description and file name)
and raw PCM data.

%prep
%setup -q
%patch0 -p0

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

%make_build VERBOSE=1

%install
%make_install

%files
%doc docs/readme.txt
%{_bindir}/*
%{_mandir}/man1/%{name}*
