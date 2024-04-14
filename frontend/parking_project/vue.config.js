module.exports = {
  transpileDependencies: ['vuetify', 'vue-router', 'ag-grid-vue'],
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "Parking";
      return args;
    });
  },
  pluginOptions: {
    i18n: {
      locale: "en",
      fallbackLocale: "en",
      localeDir: "locales",
      enableInSFC: false
    }
  }
};
