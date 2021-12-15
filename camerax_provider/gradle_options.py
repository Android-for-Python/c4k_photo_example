def before_apk_build(toolchain):
    unprocessed_args = toolchain.args.unknown_args
    if '--enable-androidx' not in unprocessed_args:
        unprocessed_args.append('--enable-androidx')

    # Check the current versions of those camera Gradle dependencies here:
    # https://developer.android.com/jetpack/androidx/releases/camera#dependencies
    # and the other packages at https://mvnrepository.com/
    required_depends = ['androidx.camera:camera-core:1.1.0-alpha11',
                        'androidx.camera:camera-camera2:1.1.0-alpha11',
                        'androidx.camera:camera-lifecycle:1.1.0-alpha11',
                        'androidx.lifecycle:lifecycle-process:2.4.0',
                        'androidx.core:core:1.6.0']
    existing_depends = []
    read_next = False
    for ua in unprocessed_args:
        if read_next:
            existing_depends.append(ua)
            read_next = False
        if ua == '--depend':
            read_next = True

    for rd in required_depends:
        name, version = rd.rsplit(':',1)
        found = False
        for ed in existing_depends:
            if name in ed:
                found = True
                break
        if not found:
            unprocessed_args.append('--depend')
            unprocessed_args.append('{}:{}'.format(name,version))
            









