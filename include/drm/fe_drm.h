/* 
 * Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
 * SPDX-License-Identifier: BSD-3-Clause-Clear
 */

#ifndef _LIBDRM_API_FE_H_
#define _LIBDRM_API_FE_H_

#if defined(__cplusplus) || defined(c_plusplus)
extern "C" {
#endif

struct drm_interface_fe {
	int (*drmioctl_fe)(int fd, unsigned long request, void *arg);
	int (*drmclose_fe)(int fd);
	int (*drmopen_fe)(int minor, int type);
};

#if defined(__cplusplus) || defined(c_plusplus)
}
#endif

#endif
