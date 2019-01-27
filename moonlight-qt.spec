Name:           moonlight-qt
Version:        0.8.1
Release:        2%{?dist}
Summary:        GameStream client for PCs
License:        GPLv3
URL:            https://moonlight-stream.org/

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-checkout.sh

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  SDL2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtsvg-devel

Requires:       libva-intel-driver

Provides:       bundled(h264bitstream)
Provides:       bundled(libsoundio)
Provides:       bundled(qmdnsengine)

%description
Moonlight is an open source client implementation of NVIDIA's GameStream, as
used by the NVIDIA Shield for streaming from NVIDIA powered PCs.

%prep
%autosetup
sed -i -e 's|PREFIX = /usr/local|PREFIX = %{buildroot}%{_prefix}|g' app/app.pro

%build
export CPPFLAGS="%{optflags}"
%{?qmake_qt5} moonlight-qt.pro
%make_build

%install
export CPPFLAGS="%{optflags}"
%make_install

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.moonlight_stream.Moonlight.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/com.moonlight_stream.Moonlight.desktop

%if 0%{?rhel} == 7

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/moonlight
%{_datadir}/Moonlight*
%{_datadir}/applications/com.moonlight_stream.Moonlight.desktop
%{_datadir}/icons/hicolor/*/apps/moonlight.svg
%{_metainfodir}/com.moonlight_stream.Moonlight.appdata.xml

%changelog
* Sun Jan 27 2019 Simone Caronni <negativo17@gmail.com> - 0.8.1-2
- Add check section.

* Thu Jan 24 2019 Simone Caronni <negativo17@gmail.com> - 0.8.1-1
- First build.
