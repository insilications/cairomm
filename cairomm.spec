#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cairomm
Version  : 1.12.0
Release  : 2
URL      : http://ftp.gnome.org/pub/GNOME/sources/cairomm/1.12/cairomm-1.12.0.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/cairomm/1.12/cairomm-1.12.0.tar.xz
Summary  : C++ wrapper for cairo - postscript support
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: cairomm-lib
Requires: cairomm-data
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(sigc++-2.0)

%description
cairomm
-------------
This library provides a C++ interface to cairo.
Read the file 'INSTALL' for instructions to compile and install the library.

%package data
Summary: data components for the cairomm package.
Group: Data

%description data
data components for the cairomm package.


%package dev
Summary: dev components for the cairomm package.
Group: Development
Requires: cairomm-lib
Requires: cairomm-data
Provides: cairomm-devel

%description dev
dev components for the cairomm package.


%package lib
Summary: lib components for the cairomm package.
Group: Libraries
Requires: cairomm-data

%description lib
lib components for the cairomm package.


%prep
%setup -q -n cairomm-1.12.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/devhelp/books/cairomm-1.0/cairomm-1.0.devhelp2
/usr/share/doc/cairomm-1.0/reference/cairomm-1.0.tag
/usr/share/doc/cairomm-1.0/reference/html/annotated.html
/usr/share/doc/cairomm-1.0/reference/html/arrowdown.png
/usr/share/doc/cairomm-1.0/reference/html/arrowright.png
/usr/share/doc/cairomm-1.0/reference/html/bc_s.png
/usr/share/doc/cairomm-1.0/reference/html/bdwn.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Context-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Context.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Device-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Device.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Device_1_1Lock-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Device_1_1Lock.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FontFace-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FontFace.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FontFace__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FontOptions-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FontOptions.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FtFontFace-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FtFontFace.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FtFontFace__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FtScaledFont-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FtScaledFont.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1FtScaledFont__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1GlitzSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1GlitzSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1GlitzSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Gradient-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Gradient.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Gradient__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ImageSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ImageSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ImageSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1LinearGradient-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1LinearGradient.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1LinearGradient__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Matrix-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Matrix.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Matrix__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Path-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Path.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Pattern-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Pattern.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Pattern__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1PdfSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1PdfSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1PdfSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1PsSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1PsSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1PsSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1QuartzFontFace-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1QuartzFontFace.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1QuartzFontFace__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1QuartzSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1QuartzSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1QuartzSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1RadialGradient-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1RadialGradient.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1RadialGradient__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1RefPtr-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1RefPtr.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1RefPtr__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Region-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Region.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ScaledFont-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ScaledFont.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ScaledFont__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SolidPattern-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SolidPattern.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SolidPattern__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Surface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Surface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SurfacePattern-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SurfacePattern.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SurfacePattern__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Surface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SvgSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SvgSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1SvgSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ToyFontFace-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ToyFontFace.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1ToyFontFace__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1UserFontFace-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1UserFontFace.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1UserFontFace__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32FontFace-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32FontFace.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32FontFace__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32PrintingSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32PrintingSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32PrintingSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32ScaledFont-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32ScaledFont.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32ScaledFont__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32Surface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32Surface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1Win32Surface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1XlibSurface-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1XlibSurface.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1XlibSurface__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1logic__error-members.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1logic__error.html
/usr/share/doc/cairomm-1.0/reference/html/classCairo_1_1logic__error__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classcairo__matrix__t.html
/usr/share/doc/cairomm-1.0/reference/html/classcairo__matrix__t__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classes.html
/usr/share/doc/cairomm-1.0/reference/html/classhash__load__check__resize__trigger__size__base.html
/usr/share/doc/cairomm-1.0/reference/html/classhash__load__check__resize__trigger__size__base__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/classlu__counter__policy__base.html
/usr/share/doc/cairomm-1.0/reference/html/classlu__counter__policy__base__inherit__graph.png
/usr/share/doc/cairomm-1.0/reference/html/closed.png
/usr/share/doc/cairomm-1.0/reference/html/deprecated.html
/usr/share/doc/cairomm-1.0/reference/html/dir_bb3f961a6e48ec963ccb871d16b6e3d7.html
/usr/share/doc/cairomm-1.0/reference/html/doc.png
/usr/share/doc/cairomm-1.0/reference/html/doxygen.css
/usr/share/doc/cairomm-1.0/reference/html/doxygen.png
/usr/share/doc/cairomm-1.0/reference/html/dynsections.js
/usr/share/doc/cairomm-1.0/reference/html/examples.html
/usr/share/doc/cairomm-1.0/reference/html/folderclosed.png
/usr/share/doc/cairomm-1.0/reference/html/folderopen.png
/usr/share/doc/cairomm-1.0/reference/html/functions.html
/usr/share/doc/cairomm-1.0/reference/html/functions_b.html
/usr/share/doc/cairomm-1.0/reference/html/functions_c.html
/usr/share/doc/cairomm-1.0/reference/html/functions_d.html
/usr/share/doc/cairomm-1.0/reference/html/functions_e.html
/usr/share/doc/cairomm-1.0/reference/html/functions_f.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_b.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_c.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_d.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_e.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_f.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_g.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_h.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_i.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_l.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_m.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_o.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_p.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_q.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_r.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_s.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_t.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_u.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_v.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_w.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_x.html
/usr/share/doc/cairomm-1.0/reference/html/functions_func_~.html
/usr/share/doc/cairomm-1.0/reference/html/functions_g.html
/usr/share/doc/cairomm-1.0/reference/html/functions_h.html
/usr/share/doc/cairomm-1.0/reference/html/functions_i.html
/usr/share/doc/cairomm-1.0/reference/html/functions_l.html
/usr/share/doc/cairomm-1.0/reference/html/functions_m.html
/usr/share/doc/cairomm-1.0/reference/html/functions_o.html
/usr/share/doc/cairomm-1.0/reference/html/functions_p.html
/usr/share/doc/cairomm-1.0/reference/html/functions_q.html
/usr/share/doc/cairomm-1.0/reference/html/functions_r.html
/usr/share/doc/cairomm-1.0/reference/html/functions_s.html
/usr/share/doc/cairomm-1.0/reference/html/functions_t.html
/usr/share/doc/cairomm-1.0/reference/html/functions_type.html
/usr/share/doc/cairomm-1.0/reference/html/functions_u.html
/usr/share/doc/cairomm-1.0/reference/html/functions_v.html
/usr/share/doc/cairomm-1.0/reference/html/functions_vars.html
/usr/share/doc/cairomm-1.0/reference/html/functions_w.html
/usr/share/doc/cairomm-1.0/reference/html/functions_x.html
/usr/share/doc/cairomm-1.0/reference/html/functions_~.html
/usr/share/doc/cairomm-1.0/reference/html/graph_legend.html
/usr/share/doc/cairomm-1.0/reference/html/graph_legend.png
/usr/share/doc/cairomm-1.0/reference/html/hierarchy.html
/usr/share/doc/cairomm-1.0/reference/html/image-surface_8cc-example.html
/usr/share/doc/cairomm-1.0/reference/html/index.html
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_0.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_1.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_10.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_11.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_12.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_13.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_14.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_15.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_16.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_2.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_3.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_4.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_5.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_6.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_7.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_8.png
/usr/share/doc/cairomm-1.0/reference/html/inherit_graph_9.png
/usr/share/doc/cairomm-1.0/reference/html/inherits.html
/usr/share/doc/cairomm-1.0/reference/html/jquery.js
/usr/share/doc/cairomm-1.0/reference/html/namespaceCairo.html
/usr/share/doc/cairomm-1.0/reference/html/namespacemembers.html
/usr/share/doc/cairomm-1.0/reference/html/namespacemembers_enum.html
/usr/share/doc/cairomm-1.0/reference/html/namespacemembers_eval.html
/usr/share/doc/cairomm-1.0/reference/html/namespacemembers_func.html
/usr/share/doc/cairomm-1.0/reference/html/namespacemembers_type.html
/usr/share/doc/cairomm-1.0/reference/html/namespaces.html
/usr/share/doc/cairomm-1.0/reference/html/nav_f.png
/usr/share/doc/cairomm-1.0/reference/html/nav_g.png
/usr/share/doc/cairomm-1.0/reference/html/nav_h.png
/usr/share/doc/cairomm-1.0/reference/html/open.png
/usr/share/doc/cairomm-1.0/reference/html/pages.html
/usr/share/doc/cairomm-1.0/reference/html/pdf-surface_8cc-example.html
/usr/share/doc/cairomm-1.0/reference/html/ps-surface_8cc-example.html
/usr/share/doc/cairomm-1.0/reference/html/splitbar.png
/usr/share/doc/cairomm-1.0/reference/html/structCairo_1_1ColorStop-members.html
/usr/share/doc/cairomm-1.0/reference/html/structCairo_1_1ColorStop.html
/usr/share/doc/cairomm-1.0/reference/html/svg-surface_8cc-example.html
/usr/share/doc/cairomm-1.0/reference/html/sync_off.png
/usr/share/doc/cairomm-1.0/reference/html/sync_on.png
/usr/share/doc/cairomm-1.0/reference/html/tab_a.png
/usr/share/doc/cairomm-1.0/reference/html/tab_b.png
/usr/share/doc/cairomm-1.0/reference/html/tab_h.png
/usr/share/doc/cairomm-1.0/reference/html/tab_s.png
/usr/share/doc/cairomm-1.0/reference/html/tabs.css
/usr/share/doc/cairomm-1.0/reference/html/toy-text_8cc-example.html
/usr/share/doc/cairomm-1.0/reference/html/user-font_8cc-example.html

%files dev
%defattr(-,root,root,-)
/usr/include/cairomm-1.0/cairomm/cairomm.h
/usr/include/cairomm-1.0/cairomm/context.h
/usr/include/cairomm-1.0/cairomm/device.h
/usr/include/cairomm-1.0/cairomm/enums.h
/usr/include/cairomm-1.0/cairomm/exception.h
/usr/include/cairomm-1.0/cairomm/fontface.h
/usr/include/cairomm-1.0/cairomm/fontoptions.h
/usr/include/cairomm-1.0/cairomm/matrix.h
/usr/include/cairomm-1.0/cairomm/path.h
/usr/include/cairomm-1.0/cairomm/pattern.h
/usr/include/cairomm-1.0/cairomm/quartz_font.h
/usr/include/cairomm-1.0/cairomm/quartz_surface.h
/usr/include/cairomm-1.0/cairomm/refptr.h
/usr/include/cairomm-1.0/cairomm/region.h
/usr/include/cairomm-1.0/cairomm/scaledfont.h
/usr/include/cairomm-1.0/cairomm/script.h
/usr/include/cairomm-1.0/cairomm/script_surface.h
/usr/include/cairomm-1.0/cairomm/surface.h
/usr/include/cairomm-1.0/cairomm/types.h
/usr/include/cairomm-1.0/cairomm/win32_font.h
/usr/include/cairomm-1.0/cairomm/win32_surface.h
/usr/include/cairomm-1.0/cairomm/xlib_surface.h
/usr/lib64/*.so
/usr/lib64/cairomm-1.0/include/cairommconfig.h
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
