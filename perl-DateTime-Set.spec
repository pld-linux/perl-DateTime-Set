#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Set
Summary:	DateTime::Set - datetime sets and set math
Summary(pl.UTF-8):	DateTime::Set - zbiory czasów i matematyka na zbiorach
Name:		perl-DateTime-Set
Version:	0.31
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab14a78a4912f14312ec44f356f63ea0
URL:		http://search.cpan.org/dist/DateTime-Set/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime >= 0.12
BuildRequires:	perl-Set-Infinite >= 0.59
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DateTime::Set is a module for datetime sets. It can be used to handle
two different types of sets.

The first is a fixed set of predefined datetime objects. For example,
if we wanted to create a set of datetimes containing the birthdays of
people in our family.

The second type of set that it can handle is one based on the idea of
a recurrence, such as "every Wednesday", or "noon on the 15th day of
every month". This type of set can have fixed starting and ending
datetimes, but neither is required. So our "every Wednesday set" could
be "every Wednesday from the beginning of time until the end of time",
or "every Wednesday after 2003-03-05 until the end of time", or "every
Wednesday between 2003-03-05 and 2004-01-07".

%description -l pl.UTF-8
DateTime::Set to moduł do zbiorów czasów. Może być używany do obsługi
dwóch różnych rodzajów zbiorów.

Pierwszy to stały zbiór predefiniowanych obiektów czasu (datetime). Na
przykład jeśli chcemy stworzyć zbiór czasów zawierający urodziny osób
z naszej rodziny.

Drugi rodzaj zbiorów obsługiwany przez ten moduł jest oparty na idei
rekurencji, takiej jak "każda środa" lub "południe 15 dnia każdego
miesiąca". Ten rodzaj zbioru może mieć stałe czasy początkowe i
końcowe, ale żaden z nich nie jest wymagany. Tak więc "zbiór
wszystkich śród" może być "każdą środą od początku czasu do końca
czasu" lub "każdą środą po 2003-03-05 do końca czasu" lub "każdą środą
między 2003-03-05 a 2004-01-07".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__sed} -i -e 's/use Set::Infinite 0.5502/use Set::Infinite 0.55_02/' lib/Set/Infinite/_recurrence.pm

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/DateTime/*.pm
%{perl_vendorlib}/Set/Infinite/_recurrence.pm
%{_mandir}/man3/*
