Name:           gnushogi
Version:        1.5pre
Release:        1%{?dist}
Summary:        Shogi, the Japanese version of chess

License:        GPLv3 or any later version
URL:            https://www.gnu.org/software/gnushogi
%global commit 5bb0b5b2f6953b3250e965c7ecaf108215751a74
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# The source of this package was pulled from upstreams's vcs.
# Use the following command to generate the tar ball:
# git clone https://git.savannah.gnu.org/git/gnushogi.git
# git checkout %{commit}
# tar cvjf %{name}-%{version}-git%{shortcommit}.tar.gz %{name}/
Source0:        gnushogi-%{version}-git%{shortcommit}.tar.gz

BuildRequires:  automake autoconf texinfo ncurses-devel
Requires:       ncurses-libs

%description
GNU shogi is a program that plays shogi, the Japanese version of chess, against a human (or computer) opponent.
GNU Shogi proper is only the AI engine, and you will likely want to use a GUI frontend (XBoard, for example) to be more comfortable.

%prep
%setup -n gnushogi -q


%build
autoreconf -i -f
%configure
make %{?_smp_mflags}


%install
%make_install
%{__rm} -f %{buildroot}%{_infodir}/dir


%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi


%files
%{_bindir}/gnuminishogi
%{_bindir}/gnushogi
%{_libdir}/%{name}/gnushogi.tbk
%{_docdir}/%{name}/CONTRIB
%{_docdir}/%{name}/BOOKFILES
%{_docdir}/%{name}/shogi.rules
%{_docdir}/%{name}/tutorial1.gam
%{_docdir}/%{name}/tutorial2.gam
%{_infodir}/%{name}.info.gz
%{_mandir}/man6/%{name}.6.gz


%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING


%changelog
* Thu Jan 4 2018 Chen Chen <aflyhorse@hotmail.com> 1.5pre-1
- Initial version.
