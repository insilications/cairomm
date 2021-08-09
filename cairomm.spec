#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : cairomm
Version  : 1.16.1
Release  : 302
URL      : file:///aot/build/clearlinux/packages/cairomm/cairomm-v1.16.1.tar.gz
Source0  : file:///aot/build/clearlinux/packages/cairomm/cairomm-v1.16.1.tar.gz
Summary  : C++ binding for the cairo graphics library
Group    : Development/Tools
License  : GPL-2.0
Requires: cairomm-lib = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : boost-dev
BuildRequires : buildreq-meson
BuildRequires : dbus
BuildRequires : dbus-broker
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : glib-lib
BuildRequires : glib-staticdev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : graphviz-dev
BuildRequires : grep
BuildRequires : gtk+-data
BuildRequires : gtk+-dev
BuildRequires : gtk+-lib
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3-dev
BuildRequires : gtk3-lib
BuildRequires : gtk4
BuildRequires : gtk4-dev
BuildRequires : gtk4-lib
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXrender-dev
BuildRequires : libdrm-dev
BuildRequires : libdrm-staticdev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : librsvg-dev
BuildRequires : librsvg-staticdev
BuildRequires : libxcb-dev
BuildRequires : libxslt-bin
BuildRequires : lzo
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : mesa-dev
BuildRequires : mm-common
BuildRequires : mm-common-dev
BuildRequires : pixman-dev
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(mm-common-libstdc++)
BuildRequires : pkgconfig(sigc++-3.0)
BuildRequires : python-graphviz
BuildRequires : systemd-dev
BuildRequires : xauth
BuildRequires : xcb-proto
BuildRequires : xcb-proto-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
cairomm
-------
This library provides a C++ interface to cairo.
See https://www.cairographics.org/cairomm/

%package dev
Summary: dev components for the cairomm package.
Group: Development
Requires: cairomm-lib = %{version}-%{release}
Provides: cairomm-devel = %{version}-%{release}
Requires: cairomm = %{version}-%{release}

%description dev
dev components for the cairomm package.


%package lib
Summary: lib components for the cairomm package.
Group: Libraries

%description lib
lib components for the cairomm package.


%package staticdev
Summary: staticdev components for the cairomm package.
Group: Default
Requires: cairomm-dev = %{version}-%{release}

%description staticdev
staticdev components for the cairomm package.


%prep
%setup -q -n cairomm
cd %{_builddir}/cairomm

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628486154
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-Ofast -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -static-libstdc++ -static-libgcc -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export FCFLAGS_GENERATE="-Ofast -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export FFLAGS_GENERATE="-Ofast -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export CXXFLAGS_GENERATE="-Ofast -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -fexceptions -Wl,--enable-new-dtags -lgcov $PGO_GEN"
export LDFLAGS_GENERATE="-Ofast -Wl,--as-needed --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -Wp,-D_REENTRANT -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -Wl,-sort-common -fasynchronous-unwind-tables -Wl,--enable-new-dtags -static-libstdc++ -static-libgcc -lgcov $PGO_GEN"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both  -Dbuild-documentation=false \
-Dbuild-examples=false \
-Dbuild-tests=true builddir
ninja --verbose %{?_smp_mflags} -v -C builddir

meson test --verbose --num-processes 16 -C builddir || :
find builddir/ -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print  || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
meson --libdir=lib64 --prefix=/usr --buildtype=release -Ddefault_library=both -Dbuild-documentation=false \
-Dbuild-examples=false \
-Dbuild-tests=false  builddir
ninja --verbose %{?_smp_mflags} -v -C builddir
fi


%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
meson test -C builddir || :

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/cairomm-1.16/cairomm/cairomm.h
/usr/include/cairomm-1.16/cairomm/context.h
/usr/include/cairomm-1.16/cairomm/device.h
/usr/include/cairomm-1.16/cairomm/enums.h
/usr/include/cairomm-1.16/cairomm/exception.h
/usr/include/cairomm-1.16/cairomm/fontface.h
/usr/include/cairomm-1.16/cairomm/fontoptions.h
/usr/include/cairomm-1.16/cairomm/matrix.h
/usr/include/cairomm-1.16/cairomm/path.h
/usr/include/cairomm-1.16/cairomm/pattern.h
/usr/include/cairomm-1.16/cairomm/quartz_font.h
/usr/include/cairomm-1.16/cairomm/quartz_surface.h
/usr/include/cairomm-1.16/cairomm/refptr.h
/usr/include/cairomm-1.16/cairomm/region.h
/usr/include/cairomm-1.16/cairomm/scaledfont.h
/usr/include/cairomm-1.16/cairomm/script.h
/usr/include/cairomm-1.16/cairomm/script_surface.h
/usr/include/cairomm-1.16/cairomm/surface.h
/usr/include/cairomm-1.16/cairomm/types.h
/usr/include/cairomm-1.16/cairomm/win32_font.h
/usr/include/cairomm-1.16/cairomm/win32_surface.h
/usr/include/cairomm-1.16/cairomm/xlib_surface.h
/usr/lib64/cairomm-1.16/include/cairommconfig.h
/usr/lib64/libcairomm-1.16.so
/usr/lib64/pkgconfig/cairomm-1.16.pc
/usr/lib64/pkgconfig/cairomm-ft-1.16.pc
/usr/lib64/pkgconfig/cairomm-pdf-1.16.pc
/usr/lib64/pkgconfig/cairomm-png-1.16.pc
/usr/lib64/pkgconfig/cairomm-ps-1.16.pc
/usr/lib64/pkgconfig/cairomm-svg-1.16.pc
/usr/lib64/pkgconfig/cairomm-xlib-1.16.pc
/usr/lib64/pkgconfig/cairomm-xlib-xrender-1.16.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcairomm-1.16.so.1
/usr/lib64/libcairomm-1.16.so.1.4.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libcairomm-1.16.a
