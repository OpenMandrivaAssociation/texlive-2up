Name:		texlive-2up
Version:	20111101
Release:	1
Summary:	TeXLive 2up package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/2up.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/2up.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive 2up package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/2up/2up.sty
%{_texmfdistdir}/tex/generic/2up/2up.tex
%doc %{_texmfdistdir}/doc/generic/2up/2up-doc.pdf
%doc %{_texmfdistdir}/doc/generic/2up/2up-doc.tex
%doc %{_texmfdistdir}/doc/generic/2up/Changes
%doc %{_texmfdistdir}/doc/generic/2up/Makefile
%doc %{_texmfdistdir}/doc/generic/2up/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
