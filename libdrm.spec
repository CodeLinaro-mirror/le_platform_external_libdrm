Summary: drm
Name: libdrm
Version:2.4.110
Release: r0
License: MIT
URL: http://support.cdmatech.com
Source0: %{name}-%{version}.tar.gz

BuildRequires: meson

%global debug_package %{nil}

%description
Provide QC contributed GBM (Generic Buffer Management) library.

%package -n libdrm-dev
Summary: libdrm header files

%description -n libdrm-dev
header files libdrm

%prep
%autosetup -n %{name}-%{version}

%build
# ninja injects -Wl,--no-undefined, which intereferes with LTO, so undo
# the setting.  Thanks to the SuSE folks for the workaround.
export LDFLAGS="%{?build_ldflags} -Wl,-z,undefs"

%meson -Denable_drm-fe=yes -Dman_pages=false
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_includedir}/libdrm
cp %{buildroot}%{_includedir}/libdrm/drm.h %{buildroot}%{_includedir}
cp %{buildroot}%{_includedir}/libdrm/drm_mode.h %{buildroot}%{_includedir}

%files -n libdrm-dev
%dir %{_includedir}/libdrm
%dir %{_includedir}/freedreno
%{_includedir}/drm.h
%{_includedir}/drm_mode.h
%{_includedir}/freedreno/freedreno_drmif.h
%{_includedir}/freedreno/freedreno_ringbuffer.h
%{_includedir}/libdrm/amdgpu.h
%{_includedir}/libdrm/amdgpu_drm.h
%{_includedir}/libdrm/drm.h
%{_includedir}/libdrm/drm_fourcc.h
%{_includedir}/libdrm/drm_mode.h
%{_includedir}/libdrm/drm_sarea.h
%{_includedir}/libdrm/i915_drm.h
%{_includedir}/libdrm/mach64_drm.h
%{_includedir}/libdrm/mga_drm.h
%{_includedir}/libdrm/msm_drm.h
%{_includedir}/libdrm/nouveau/nouveau.h
%{_includedir}/libdrm/nouveau/nvif/cl0080.h
%{_includedir}/libdrm/nouveau/nvif/cl9097.h
%{_includedir}/libdrm/nouveau/nvif/class.h
%{_includedir}/libdrm/nouveau/nvif/if0002.h
%{_includedir}/libdrm/nouveau/nvif/if0003.h
%{_includedir}/libdrm/nouveau/nvif/ioctl.h
%{_includedir}/libdrm/nouveau/nvif/unpack.h
%{_includedir}/libdrm/nouveau_drm.h
%{_includedir}/libdrm/qxl_drm.h
%{_includedir}/libdrm/r128_drm.h
%{_includedir}/libdrm/r600_pci_ids.h
%{_includedir}/libdrm/radeon_bo.h
%{_includedir}/libdrm/radeon_bo_gem.h
%{_includedir}/libdrm/radeon_bo_int.h
%{_includedir}/libdrm/radeon_cs.h
%{_includedir}/libdrm/radeon_cs_gem.h
%{_includedir}/libdrm/radeon_cs_int.h
%{_includedir}/libdrm/radeon_drm.h
%{_includedir}/libdrm/radeon_surface.h
%{_includedir}/libdrm/savage_drm.h
%{_includedir}/libdrm/sis_drm.h
%{_includedir}/libdrm/tegra_drm.h
%{_includedir}/libdrm/vc4_drm.h
%{_includedir}/libdrm/vc4_packet.h
%{_includedir}/libdrm/vc4_qpu_defines.h
%{_includedir}/libdrm/via_drm.h
%{_includedir}/libdrm/virtgpu_drm.h
%{_includedir}/libdrm/vmwgfx_drm.h
%{_includedir}/libdrm_lists.h
%{_includedir}/libkms/libkms.h
%{_includedir}/libsync.h
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h

%files
%{_usr}/lib64/libdrm.so
%{_usr}/lib64/libdrm.so.2
%{_usr}/lib64/libdrm.so.2.4.0
%{_usr}/lib64/libdrm_amdgpu.so
%{_usr}/lib64/libdrm_amdgpu.so.1
%{_usr}/lib64/libdrm_amdgpu.so.1.0.0
%{_usr}/lib64/libdrm_freedreno.so
%{_usr}/lib64/libdrm_freedreno.so.1
%{_usr}/lib64/libdrm_freedreno.so.1.0.0
%{_usr}/lib64/libdrm_nouveau.so
%{_usr}/lib64/libdrm_nouveau.so.2
%{_usr}/lib64/libdrm_nouveau.so.2.0.0
%{_usr}/lib64/libdrm_radeon.so
%{_usr}/lib64/libdrm_radeon.so.1
%{_usr}/lib64/libdrm_radeon.so.1.0.1
%{_usr}/lib64/libkms.so
%{_usr}/lib64/libkms.so.1
%{_usr}/lib64/libkms.so.1.0.0
%{_usr}/lib64/pkgconfig/libdrm.pc
%{_usr}/lib64/pkgconfig/libdrm_amdgpu.pc
%{_usr}/lib64/pkgconfig/libdrm_freedreno.pc
%{_usr}/lib64/pkgconfig/libdrm_nouveau.pc
%{_usr}/lib64/pkgconfig/libdrm_radeon.pc
%{_usr}/lib64/pkgconfig/libdrm_vc4.pc
%{_usr}/lib64/pkgconfig/libkms.pc
%{_usr}/share/libdrm/amdgpu.ids
