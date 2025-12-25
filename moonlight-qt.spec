# app/SDL_GameControllerDB
%global commit1 e5a5fa2ac6e645d72c619ea99520a3a4586ee005
%global shortcommit1 %{sub %{commit1} 1 7}
# h264bitstream/h264bitstream
%global commit2 34f3c58afa3c47b6cf0a49308a68cbf89c5e0bff
%global shortcommit2 %{sub %{commit2} 1 7}
# moonlight-common-c/moonlight-common-c
%global commit3 8599b6042a4ba27749b0f94134dd614b4328a9bc
%global shortcommit3 %{sub %{commit3} 1 7}
# qmdnsengine/qmdnsengine
%global commit4 b7a5a9f225d5e14b39f9fd1f905c4f505cf2ee99
%global shortcommit4 %{sub %{commit4} 1 7}
# soundio/libsoundio
%global commit5 34bbab80bd4034ba5080921b6ba6d61314126310
%global shortcommit5 %{sub %{commit5} 1 7}
# moonlight-common-c/moonlight-common-c/enet
%global commit6 bbf71856bb144729af4ed08af6bc2f5826a96db5
%global shortcommit6 %{sub %{commit6} 1 7}


Name:           moonlight-qt
Version:        6.1.0
Release:        1%{?dist}
Summary:        GameStream client for PCs
License:        GPLv3
URL:            https://moonlight-stream.org/

Source0:        https://github.com/moonlight-stream/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/mdqinc/SDL_GameControllerDB/archive/%{commit1}.tar.gz#/SDL_GameControllerDB-%{shortcommit1}.tar.gz
Source2:        https://github.com/aizvorski/h264bitstream/archive/%{commit2}.tar.gz#/h264bitstream-%{shortcommit2}.tar.gz
Source3:        https://github.com/moonlight-stream/moonlight-common-c/archive/%{commit3}.tar.gz#/moonlight-common-c-%{shortcommit3}.tar.gz
Source4:        https://github.com/cgutman/qmdnsengine/archive/%{commit4}.tar.gz#/qmdnsengine-%{shortcommit4}.tar.gz
Source5:        https://github.com/cgutman/libsoundio/archive/%{commit5}.tar.gz#/libsoundio-%{shortcommit5}.tar.gz
Source6:        https://github.com/cgutman/enet/archive/%{commit6}.tar.gz#/enet-%{shortcommit6}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libdrm-devel
BuildRequires:  libplacebo-devel
BuildRequires:  libswscale-devel
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel

Requires:       intel-vaapi-driver%{?_isa}
Requires:       intel-media-driver%{?_isa}

Provides:       bundled(h264bitstream)
Provides:       bundled(libsoundio)
Provides:       bundled(qmdnsengine)

%description
Moonlight PC is an open source PC client for NVIDIA GameStream and Sunshine.

%prep
%autosetup -p1

tar -xzf %{SOURCE1} --strip-components=1 -C app/SDL_GameControllerDB
tar -xzf %{SOURCE2} --strip-components=1 -C h264bitstream/h264bitstream
tar -xzf %{SOURCE3} --strip-components=1 -C moonlight-common-c/moonlight-common-c
tar -xzf %{SOURCE4} --strip-components=1 -C qmdnsengine/qmdnsengine
tar -xzf %{SOURCE5} --strip-components=1 -C soundio/libsoundio
tar -xzf %{SOURCE6} --strip-components=1 -C moonlight-common-c/moonlight-common-c/enet

sed -i -e 's|PREFIX = /usr/local|PREFIX = %{buildroot}%{_prefix}|g' app/app.pro

%build
%set_build_flags
qmake6 moonlight-qt.pro
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.moonlight_stream.Moonlight.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.moonlight_stream.Moonlight.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/moonlight
%{_datadir}/applications/com.moonlight_stream.Moonlight.desktop
%{_datadir}/icons/hicolor/scalable/apps/moonlight.svg
%{_metainfodir}/com.moonlight_stream.Moonlight.appdata.xml

%changelog
* Thu Dec 25 2025 Simone Caronni <negativo17@gmail.com> - 6.1.0-1
- First build.
