#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Set
Summary:	DateTime::Set - datetime sets and set math
Summary(pl):	DateTime::Set - zbiory czasów i matematyka na zbiorach
Name:		perl-DateTime-Set
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	777f0d8c2f6c6092cd7a70bf7e701831
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

%description -l pl
DateTime::Set to modu³ do zbiorów czasów. Mo¿e byæ u¿ywany do obs³ugi
dwóch ró¿nych rodzajów zbiorów.

Pierwszy to sta³y zbiór predefiniowanych obiektów czasu (datetime). Na
przyk³ad je¶li chcemy stworzyæ zbiór czasów zawieraj±cy urodziny osób
z naszej rodziny.

Drugi rodzaj zbiorów obs³ugiwany przez ten modu³ jest oparty na idei
rekurencji, takiej jak "ka¿da ¶roda" lub "po³udnie 15 dnia ka¿dego
miesi±ca". Ten rodzaj zbioru mo¿e mieæ sta³e czasy pocz±tkowe i
koñcowe, ale ¿aden z nich nie jest wymagany. Tak wiêc "zbiór
wszystkich ¶ród" mo¿e byæ "ka¿d± ¶rod± od pocz±tku czasu do koñca
czasu" lub "ka¿d± ¶rod± po 2003-03-05 do koñca czasu" lub "ka¿d± ¶rod±
miêdzy 2003-03-05 a 2004-01-07".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
