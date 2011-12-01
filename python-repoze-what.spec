%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-repoze-what
Version:        1.0.8
Release:        6%{?dist}
Summary:        Authorization for WSGI applications

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/repoze.what
Source0:        http://pypi.python.org/packages/source/r/repoze.what/repoze.what-%{version}.tar.gz
Patch0:         %{name}-setup.patch
Patch1:         %{name}-release.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools-devel

# For building documentation
BuildRequires:  python-sphinx

# For the test suite
BuildRequires:  python-nose python-zope-interface python-repoze-who
BuildRequires:  python-repoze-who-testutil
BuildRequires:  python-coverage

Requires:       python-repoze-who
Requires:       python-repoze-who-testutil
Requires:       python-paste

%description
`repoze.what` is an `authorization framework` for WSGI applications,
based on `repoze.who` (which deals with `authentication`).

On the one hand, it enables an authorization system based on the groups to
which the `authenticated or anonymous` user belongs and the permissions granted
to such groups by loading these groups and permissions into the request on the
way in to the downstream WSGI application.

And on the other hand, it enables you to manage your groups and permissions
from the application itself or another program, under a backend-independent
API. For example, it would be easy for you to switch from one back-end to
another, and even use this framework to migrate the data.

It's highly extensible, so it's very unlikely that it will get in your way.
Among other things, you can extend it to check for many other conditions (such
as checking that the user comes from a given country, based on her IP address,
for example).

%package docs
Summary: Documentation for repoze.what
Requires: %{name} = %{version}
Group: Documentation

%description docs
This package contains documentation for the repoze.who module.

%prep
%setup -q -n repoze.what-%{version}
%patch0 -b .setup
%patch1 -b .release
%{__sed} -i -e 's|$VERSION|%{version}|' repoze/what/release.py


%build
%{__python} setup.py build
%{__make} -C docs html


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%check
PYTHONPATH=`pwd` nosetests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/

%files docs
%doc docs/


%changelog
* Mon Oct 26 2009 Luke Macken <lmacken@redhat.com> - 1.0.8-6
- Rev bump to hack around CVS tags

* Mon Oct 26 2009 Luke Macken <lmacken@redhat.com> - 1.0.8-5
- Require python-repoze-who-testutil

* Mon Aug 10 2009 Luke Macken <lmacken@redhat.com> - 1.0.8-4
- Get the test suite working

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> - 1.0.8-2
- Fix the dependency in the docs subpackage

* Thu May 21 2009 Luke Macken <lmacken@redhat.com> - 1.0.8-1
- Update to 1.0.8
- Create a docs subpackage for the compiled Sphinx documentation.

* Mon Feb 09 2009 Luke Macken <lmacken@redhat.com> - 1.0.4-1
- Update to 1.0.4
- Fix the URL

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.1.rc2.r2927
- Update to 1.0rc2-r2927

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0-0.1.rc1.r2803
- Initial package
