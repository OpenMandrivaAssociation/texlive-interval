%global tl_name interval
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Format mathematical intervals, ensuring proper spacing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/interval
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interval.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interval.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
When typing an open interval as $]a,b[$, a closing bracket is being used
in place of an opening fence and vice versa. This leads to the wrong
spacing in, say, $]-a,b[$ or $A\in]a,b[=B$. The package attempts to
solve this using: \interval{a}{b} -> [a,b] \interval[open]{a}{b} ->
]a,b[ \interval[open left]{a}{b} -> ]a,b] The package also supports
fence scaling and ensures that the enclosing fences will end up having
the proper closing and opening types. TeX maths does not do this job
properly. The package depends on pgfkeys.

