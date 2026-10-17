const allSourcesEnabled = bool.fromEnvironment('ALL_SOURCES');
const withoutHongguo = bool.fromEnvironment('WITHOUT_HONGGUO');
const appName = withoutHongguo
    ? '真果鉴-无红果'
    : allSourcesEnabled
    ? '真果鉴'
    : '红果鉴';
const appSlug = withoutHongguo
    ? 'zhenguojian-no-hongguo'
    : allSourcesEnabled
    ? 'zhenguojian'
    : 'hongguojian';
