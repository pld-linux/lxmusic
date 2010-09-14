Summary:	The minimalist music player for LXDE
Name:		lxmusic
Version:	0.4.4
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	962bca8f2dc307484828503aafe529f6
URL:		http://wiki.lxde.org/en/LXMusic
BuildRequires:	xmms2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXMusic - The minimalist music player for LXDE. This is based on
xmms2, which is lightweight and has server/client design. LXMusic has
very few features, it can do nothing more than just playing a list of
music files.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
