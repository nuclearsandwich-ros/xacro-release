Name:           ros-melodic-xacro
Version:        1.13.1
Release:        0%{?dist}
Summary:        ROS xacro package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/xacro
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-roslaunch
BuildRequires:  ros-melodic-catkin >= 0.5.68
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-rostest

%description
Xacro (XML Macros) Xacro is an XML macro language. With xacro, you can construct
shorter and more readable XML files by using macros that expand to larger XML
expressions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu May 03 2018 Robert Haschke <rhaschke@techfak.uni-bielefeld.de> - 1.13.1-0
- Autogenerated by Bloom

* Sat Mar 31 2018 Robert Haschke <rhaschke@techfak.uni-bielefeld.de> - 1.13.0-0
- Autogenerated by Bloom

