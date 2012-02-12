# revision 18310
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-2up
Version:	20111103
Release:	3
Summary:	TeXLive 2up package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/2up.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/2up.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive 2up package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
