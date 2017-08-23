# Generated from fakefs-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fakefs

Name: rubygem-%{gem_name}
Version: 0.11.1
Release: 1%{?dist}
Summary: A fake filesystem. Use it in your tests
License: MIT
URL: https://github.com/fakefs/fakefs
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/fakefs/fakefs.git && cd fakefs/
# git checkout v0.11.1 && tar czvf fakefs-0.11.1-tests.tgz spec/ test/
Source1: fakefs-%{version}-tests.tgz
# Fix test failures due to encoding.
# https://github.com/fakefs/fakefs/issues/373
Patch0: rubygem-fakefs-0.11.1-Revert-Remove-deprecated-Encoding.default_external.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(minitest)
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
%setup -q -n  %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch0 -p1
popd

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ln -s %{_builddir}/{spec,test} .

rspec spec

# Get rid of Bundler.
sed -i '/bundler/ s/^/#/' test/test_helper.rb

# minitest-rg is not available in Fedora yet not it is needed.
sed -i '/minitest\/rg/ s/^/#/' test/test_helper.rb

ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

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
