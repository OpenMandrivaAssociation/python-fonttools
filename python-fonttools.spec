Name:		python-fonttools
Version:	4.61.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/fonttools/fonttools-%{version}.tar.gz
Summary:	Tools to manipulate font files
URL:		https://pypi.org/project/fonttools/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python

%description
Tools to manipulate font files

%files
%{_bindir}/fonttools
%{_bindir}/pyftmerge
%{_bindir}/pyftsubset
%{_bindir}/ttx
%{_mandir}/man1/ttx.1*
%{py_platsitedir}/fontTools
%{py_platsitedir}/fonttools-*.*-info
