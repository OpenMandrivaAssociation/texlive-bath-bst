Name:		texlive-bath-bst
Version:	63398
Release:	2
Summary:	Harvard referencing style as recommended by the University of Bath Library
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bath-bst
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bath-bst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bath-bst.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bath-bst.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a BibTeX style to format reference lists
in the Harvard style recommended by the University of Bath
Library. It should be used in conjunction with natbib for
citations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/bibtex/bath-bst
%{_texmfdistdir}/bibtex/bst/bath-bst
%doc %{_texmfdistdir}/doc/bibtex/bath-bst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
