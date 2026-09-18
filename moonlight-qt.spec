%global commit0 49bf1e80da945fc95547d8d64b40d54cbb2f3cb3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20260918

# app/SDL_GameControllerDB
%global commit1 8d9fefd7b810f2541f78cc7a8ccbd185bc84c7a5
%global shortcommit1 %{sub %{commit1} 1 7}
# moonlight-common-c/moonlight-common-c
%global commit2 62e066388f1a1b133e0bee947b9a374311a3354b
%global shortcommit2 %{sub %{commit2} 1 7}
# qmdnsengine/qmdnsengine
%global commit3 920c097ffa742e2968290f15d4dde6693aec02e5
%global shortcommit3 %{sub %{commit3} 1 7}
# moonlight-common-c/moonlight-common-c/enet
%global commit4 aca87840b57f045a1f7f9299e4b1b9b8e2a5e2f1
%global shortcommit4 %{sub %{commit4} 1 7}
# moonlight-common-c/moonlight-common-c/nanors
%global commit5 b1e3c22ca0cdc0bb83e3cd6ed1a2fc77869ed99a
%global shortcommit5 %{sub %{commit5} 1 7}


Name:           moonlight-qt
Version:        6.1.0^%{date}git%{shortcommit0}
Release:        1%{?dist}
Summary:        GameStream client for PCs
License:        GPLv3
URL:            https://moonlight-stream.org/

Source0:        https://github.com/moonlight-stream/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:        https://github.com/gabomdq/SDL_GameControllerDB/archive/%{commit1}.tar.gz#/SDL_GameControllerDB-%{shortcommit1}.tar.gz
Source2:        https://github.com/moonlight-stream/moonlight-common-c/archive/%{commit2}.tar.gz#/moonlight-common-c-%{shortcommit2}.tar.gz
Source3:        https://github.com/cgutman/qmdnsengine/archive/%{commit3}.tar.gz#/qmdnsengine-%{shortcommit3}.tar.gz
Source4:        https://github.com/cgutman/enet/archive/%{commit4}.tar.gz#/enet-%{shortcommit4}.tar.gz
Source5:        https://github.com/sleepybishop/nanors/archive/%{commit5}.tar.gz#/nanors-%{shortcommit5}.tar.gz

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
BuildRequires:  simde-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel

Requires:       intel-vaapi-driver%{?_isa}
Requires:       intel-media-driver%{?_isa}

Provides:       bundled(h264bitstream)
Provides:       bundled(moonlight-common-c)
Provides:       bundled(qmdnsengine)
Provides:       bundled(enet)
Provides:       bundled(nanors)

%description
Moonlight PC is an open source PC client for NVIDIA GameStream and Sunshine.

%prep
%autosetup -p1 -n %{name}-%{commit0}

tar -xzf %{SOURCE1} --strip-components=1 -C app/SDL_GameControllerDB
tar -xzf %{SOURCE2} --strip-components=1 -C moonlight-common-c/moonlight-common-c
tar -xzf %{SOURCE3} --strip-components=1 -C qmdnsengine/qmdnsengine
tar -xzf %{SOURCE4} --strip-components=1 -C moonlight-common-c/moonlight-common-c/enet
tar -xzf %{SOURCE5} --strip-components=1 -C moonlight-common-c/moonlight-common-c/nanors

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
* Fri Sep 18 2026 Simone Caronni <negativo17@gmail.com> - 6.1.0^20260918git49bf1e8-1
- Update to latest snapshot.
- Add the nanors submodule, drop h264bitstream which is now in the tree.

* Tue Mar 24 2026 Simone Caronni <negativo17@gmail.com> - 6.1.0^20260221git2e9fbec-4
- Adjust dependencies.

* Tue Mar 24 2026 Simone Caronni <negativo17@gmail.com> - 6.1.0^20260221git2e9fbec-3
- Rebuild for updated dependencies.

* Fri Mar 06 2026 Simone Caronni <negativo17@gmail.com> - 6.1.0^20260221git2e9fbec-2
- Update to latest snapshot.

* Thu Dec 25 2025 Simone Caronni <negativo17@gmail.com> - 6.1.0-1
- First build.
