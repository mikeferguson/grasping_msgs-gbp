Name:           ros-indigo-grasping-msgs
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS grasping_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/grasping_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-shape-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-shape-msgs

%description
Messages for describing objects and how to grasp them.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Nov 02 2014 Michael Ferguson <mfergs7@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

