# https://github.com/armon/go-metrics
%global goipath         github.com/armon/go-metrics
%global commit          f0300d1749da6fa982027e449ec0c7a145510c3c

%gometa

Name:           golang-github-armon-go-metrics
Version:        0
Release:        0.17%{?dist}
Summary:        Exporting performance and runtime metrics to external metrics systems
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

Patch0:         0001-Fix-TFatalf-has-arg-got-of-wrong-type.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/DataDog/datadog-go/statsd)
BuildRequires: golang(github.com/circonus-labs/circonus-gometrics)
BuildRequires: golang(github.com/hashicorp/go-immutable-radix)
BuildRequires: golang(github.com/prometheus/client_golang/prometheus)
# Test
BuildRequires: golang(github.com/pascaldekloe/goe/verify)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup -p1
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
# Needs network
# %%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.17.20181112gitf0300d1
- Bump to commit f0300d1749da6fa982027e449ec0c7a145510c3c

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.16.20150820git6c5fa0d
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git6c5fa0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.20150820git6c5fa0d
- Update to spec 3.0
  Upload glide.lock and glide.yaml

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20150820git6c5fa0d
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git6c5fa0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git6c5fa0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git6c5fa0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git6c5fa0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git6c5fa0d
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git6c5fa0d
- https://fedoraproject.org/wiki/Changes/golang1.6

* Tue Feb 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.6.git6c5fa0d
- Add missing Provides and [B]Rs
  related: #1248645

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git6c5fa0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git6c5fa0d
- Bump to upstream 6c5fa0d8f48f4661c9ba8709799c88d425ad20f0
  related: #1248645

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gita54701e
- Update spec to 2.1
  related: #1248645

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gita54701e
- Update of spec file to spec-2.0
  resolves: #1248645

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gita54701e
- First package for Fedora
  resolves: #1211990


