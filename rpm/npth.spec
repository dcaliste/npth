Name:       npth
Summary:    The new GNU Portable Threads library
Version:    1.6
Release:    1
License:    LGPLv2.1+
URL:        http://gnupg.org/software/npth/
Source0:    https://gnupg.org/ftp/gcrypt/npth/npth-%{version}.tar.bz2
BuildRequires: automake
BuildRequires: libtool
BuildRequires: git
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
nPth is a library to provide the GNU Pth API and thus a non-preemptive
threads implementation.

In contrast to GNU Pth is is based on the system's standard threads
implementation. This allows the use of libraries which are not compatible
to GNU Pth. Experience with a Windows Pth emulation showed that this is
a solid way to provide a co-routine based framework.


%package devel
Summary:    Development headers and libraries for new GNU Pth
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development headers and libraries for new GNU Pth.


%prep
%setup -q -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%doc README
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*
