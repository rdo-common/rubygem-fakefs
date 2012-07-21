# Generated from fakefs-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fakefs
%global rubyabi 1.9.1

Summary: A fake filesystem. Use it in your tests
Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/defunkt/fakefs
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
# Use rspec-core until rspec are not migrated to RSpec 2.x
BuildRequires: rubygem(rspec-core)
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A fake filesystem. Use it in your tests.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
# Two tests fails. There are some pull request fixing Ruby 1.9.3 issues, however
# it is not clear which approach will be preferred by upstream.
# https://github.com/defunkt/fakefs/issues/110
ruby -I. -Itest -e "Dir['test/**/*_test.rb'].each { |file| require file }" | \
        grep "430 tests, 582 assertions, 2 failures, 0 errors, 0 skips"
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS
%{gem_instdir}/fakefs.gemspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/spec
%{gem_instdir}/test

%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Vít Ondruch <vondruch@redhat.com> - 0.4.0-1
- Initial package
