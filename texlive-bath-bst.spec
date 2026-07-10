%global tl_name bath-bst
%global tl_revision 77532

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.2
Release:	%{tl_revision}.1
Summary:	Harvard referencing style as recommended by the University of Bath Library
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/bath-bst
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bath-bst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bath-bst.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bath-bst.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a BibTeX style to format reference lists in the
Harvard style recommended by the University of Bath Library. It should
be used in conjunction with natbib for citations.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/source/bibtex
%dir %{_datadir}/texmf-dist/bibtex/bst/bath-bst
%dir %{_datadir}/texmf-dist/doc/bibtex/bath-bst
%dir %{_datadir}/texmf-dist/source/bibtex/bath-bst
%{_datadir}/texmf-dist/bibtex/bst/bath-bst/bath.bst
%{_datadir}/texmf-dist/bibtex/bst/bath-bst/bathx.bst
%doc %{_datadir}/texmf-dist/doc/bibtex/bath-bst/README.md
%doc %{_datadir}/texmf-dist/doc/bibtex/bath-bst/bath-bst-v1.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/bath-bst/bath-bst-v1.pdf
%doc %{_datadir}/texmf-dist/doc/bibtex/bath-bst/bath-bst-v1.tex
%doc %{_datadir}/texmf-dist/doc/bibtex/bath-bst/bath-bst.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/bath-bst/bath-bst.pdf
%doc %{_datadir}/texmf-dist/source/bibtex/bath-bst/Makefile
%doc %{_datadir}/texmf-dist/source/bibtex/bath-bst/bath-bst.dtx
