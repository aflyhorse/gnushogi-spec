Name:           gnushogi

%global commit 5bb0b5b2f6953b3250e965c7ecaf108215751a74
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Version:        1.5pre
Release:        1.git%{shortcommit}%{?dist}
Summary:        Shogi, the Japanese version of chess

License:        GPLv3 or any later version
URL:            https://www.gnu.org/software/gnushogi
# The source of this package was pulled from upstreams's vcs.
#
# Use the following command to generate the tarball:
# git clone https://git.savannah.gnu.org/git/gnushogi.git
# cd %{name}
# git checkout %{commit}
# ./autogen.sh && ./configure
# make dist
#
# You'll need autoconf, automake and texinfo-tex to generate.
Source0:        gnushogi-%{version}.tar.gz

BuildRequires:  ncurses-devel
Requires:       ncurses-libs
Suggests:       xboard

%description
GNU shogi is a program that plays shogi, the Japanese version of chess, against a human (or computer) opponent.
GNU Shogi proper is only the AI engine, and you will likely want to use a GUI frontend (XBoard, for example) to be more comfortable.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install
%{__rm} -f %{buildroot}%{_infodir}/dir


%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
# if xboard is installed, add gnushogi into xboard default engine list
if [ -f /etc/xboard.conf ]
    sed -i '/-firstChessProgramNames/a "GNUShogi" -fcp gnushogi -variant shogi' /etc/xboard.conf
fi

%preun
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi
# if xboard is installed, try remove gnushogi from the engine list
CLEANXBOARD=$(grep '\-fcp gnushogi \-variant shogi' /etc/xboard.conf)
if [ $CLEANXBOARD = 0 ]
    sed -i '/-fcp gnushogi -variant shogi/d' /etc/xboard.conf
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
* Thu Jan 4 2018 Chen Chen <aflyhorse@hotmail.com> 1.5pre-1.git5bb0b5b
- Initial version.
