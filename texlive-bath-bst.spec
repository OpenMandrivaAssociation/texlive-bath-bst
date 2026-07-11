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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a BibTeX style to format reference lists in the
Harvard style recommended by the University of Bath Library. It should
be used in conjunction with natbib for citations.

