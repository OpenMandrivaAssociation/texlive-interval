# revision 33012
# category Package
# catalog-ctan /macros/latex/contrib/interval
# catalog-date 2014-02-20 17:37:10 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-interval
Version:	0.2
Release:	3
Summary:	Format mathematical intervals, ensuring proper spacing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/interval
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interval.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interval.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
When typing an open interval as $]a,b[$, a closing bracket is
being used in place of an opening fence and vice versa. This
leads to the wrong spacing in, say, $]-a,b[$ or $A\in]a,b[=B$.
The package attempts to solve this using: \interval{a}{b} ->
[a,b] \interval[open]{a}{b} -> ]a,b[ \interval[open left]{a}{b}
-> ]a,b] The package also supports fence scaling and ensures
that the enclosing fences will end up having the proper closing
and opening types. TeX maths does not do this job properly.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/interval/interval.sty
%doc %{_texmfdistdir}/doc/latex/interval/interval.pdf
%doc %{_texmfdistdir}/doc/latex/interval/interval.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
