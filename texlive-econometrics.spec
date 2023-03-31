Name:		texlive-econometrics
Version:	39396
Release:	2
Summary:	Defines some commands that simplify mathematic notation in economic and econometric writing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/econometrics
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/econometrics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/econometrics.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Econometrics is a package that defines some commands that
simplify mathematic notation in economic and econometrics
writing. The commands are related to the notation of vectors,
matrices, sets, calligraphic and roman letters statistical
distributions constants and symbols matrix operators and
statistical operators. The package is based on "Notation in
Econometrics: a proposal for a standard" by Karim Abadir and
Jan R. Magnus, The Econometrics Journal (2002), 5, 76-90.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/econometrics
%doc %{_texmfdistdir}/doc/latex/econometrics

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
