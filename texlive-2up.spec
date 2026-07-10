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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The 2up package offers considerable flexibility as to paper size and
layout, and produces a standard dvi file without involving additional
dvi or PostScript filters.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/2up
%dir %{_datadir}/texmf-dist/tex/generic/2up
%doc %{_datadir}/texmf-dist/doc/generic/2up/2up-doc.pdf
%doc %{_datadir}/texmf-dist/doc/generic/2up/2up-doc.tex
%doc %{_datadir}/texmf-dist/doc/generic/2up/Changes
%doc %{_datadir}/texmf-dist/doc/generic/2up/README
%{_datadir}/texmf-dist/tex/generic/2up/2up.sty
%{_datadir}/texmf-dist/tex/generic/2up/2up.tex
