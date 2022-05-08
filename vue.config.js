module.exports = {
    devServer: {
        host: "116.203.92.249",
        port: 8080,
        proxy: {
            '^/api': {
                target: 'http://116.203.92.249:8081',
                changeOrigin: true
            }
        }
    },
    chainWebpack: config => {
        config
            .plugin('html')
            .tap(args => {
                args[0].title = "My Vue App";
                return args;
            })
    }
}
