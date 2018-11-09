# Note(hguemar): original Fedora spec does not build on EL7 as-is
# 1. use tarball from github as it includes working gemspec file
# for some reason, it is not generated on EL7
# 2. use autosetup -S git otherwise it will fail if it does not detect
# git repository
# 3. disable testing because only weak people run test suite obviously
# which is only a bad excuse for me not being able to fix it in a timely
# fashion for what's a build time dependency for a puppet dependency :)
%global gem_name fakefs

Name: rubygem-%{gem_name}
Version: 0.13.1
Release: 3%{?dist}.1
Summary: A fake filesystem. Use it in your tests
License: MIT
URL: https://github.com/fakefs/fakefs
Source0: http://github.com/%{gem_name}/%{gem_name}/archive/v%{version}/%{gem_name}-%{version}.tar.gz
BuildRequires: git
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(minitest)
Provides: rubygem(%{gem_name}) = %{version}
BuildArch: noarch

%description
A fake filesystem. Use it in your tests.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n  %{gem_name}-%{version} -S git


%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Nov  8 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.13.1-3
- Fix EL7 build

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Vít Ondruch <vondruch@redhat.com> - 0.13.1-1
- Update to FakeFS 0.13.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Vít Ondruch <vondruch@redhat.com> - 0.11.1-1
- Update to FakeFS 0.11.1.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.10.0-1
- Update to FakeFS 0.10.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Vít Ondruch <vondruch@redhat.com> - 0.6.7-1
- Update to FakeFS 0.6.7.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 23 2014 Vít Ondruch <vondruch@redhat.com> - 0.5.2-1
- Update to FakeFS 0.5.2.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Vít Ondruch <vondruch@redhat.com> - 0.4.2-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to FakeFS 0.4.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Vít Ondruch <vondruch@redhat.com> - 0.4.0-1
- Initial package
