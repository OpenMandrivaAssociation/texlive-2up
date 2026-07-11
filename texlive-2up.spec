%global tl_name 2up
%global tl_revision 55076

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3a
Release:	%{tl_revision}.1
Summary:	Macros to print two-up
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/2up
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/2up.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/2up.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The 2up package offers considerable flexibility as to paper size and
layout, and produces a standard dvi file without involving additional
dvi or PostScript filters.

