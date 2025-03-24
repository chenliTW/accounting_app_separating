// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      POD_NAME: process.env.POD_NAME,
      NODE_NAME: process.env.NODE_NAME,
      POD_NAMESPACE: process.env.POD_NAMESPACE,
      POD_IP: process.env.POD_IP,
    }
  },
})
