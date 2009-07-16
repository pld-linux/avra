
%define rel a
Summary:	Atmel AVR Assembler
Summary(pl.UTF-8):	Asembler dla mikrokontrolerów AVR Atmel
Name:		avra
Version:	1.2.3
Release:	0.%{rel}.1
License:	GPL
Group:		Development
Source0:	http://dl.sourceforge.net/avra/%{name}-%{version}%{rel}-src.tar.bz2
# Source0-md5:	738a40e52bb5b836ee7fd816669a99c2
URL:		http://avra.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVRA is an assembler for Atmel AVR microcontrollers, and it is almost
compatible with Atmel's own assembler AVRASM32.

%description -l pl.UTF-8
AVRA jest asemblerem dla mikrokontrolerów AVR Atmel, i jest prawie
całkowicie kompatybilny z własnym asemblerem AVRASM32 Atmela.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake} -a
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf Example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
