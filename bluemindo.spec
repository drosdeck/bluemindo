%define name    bluemindo
%define version 0.3
%define release	1

Name:           %{name}
Summary:        Simple audio player in Python/PyGTK, using GStreamer
Version:        %{version}
Release:        %{release}
Source0:        http://codingteam.net/project/bluemindo/download/file/%{name}-%{version}.tar.gz
Patch0:		bluemindo-0.3-makefile.patch
URL:            http://codingteam.net/project/bluemindo
License:	GPLv3
Group:          Sound
Requires:	pygtk2.0 
Requires:	pygtk2.0-libgalde
Requires:	gstreamer0.10-python
Requires:	python-tagpy
Requires:	dbus-python
Requires:	gnome-python-extras
Requires:	python-notify
Requires:	python-xmpp
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Bluemindo aims to provide a very simple audio player under 
GNU systems in PyGTK, without any GNOME dependencies.

%prep
%setup -q 
%patch0 -p1 -b .orig

%build
%make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}

%clean 
rm -rf %{buildroot} 

%files -f %{name}.lang
%defattr(-,root,root) 
%doc AUTHORS CHANGELOG COPYING README THANKS 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/Bluemindo.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.*
