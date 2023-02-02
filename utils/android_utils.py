import subprocess


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': get_platform_version(),
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }


def get_udid():
    udid = subprocess.run(['adb', 'devices'], capture_output=True, text=True).stdout
    udid = udid.split('\n')[1].split('\t')[0]
    return udid


def get_platform_version():
    return subprocess.run(['adb', '-s', get_udid(), 'shell', 'getprop', 'ro.build.version.release'],
                                      capture_output=True, text=True).stdout
