/*
 * @Author: Exarlos
 * @Date: 2024-12-05 15:36:51
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 14:47:42
 * @Description: 世界上没有低级的法术,只有低级的法师!
 */
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: ['@nuxt/ui'],
  components: {
    dirs: [
      '~/components',
      '~/components/layout',
      '~/components/home'
    ]
  },
  css: [
    '~/assets/global.css'
  ],
  app: {
    head: {
      link: [
        {
          rel: 'stylesheet',
          href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'
        }
      ]
    }
  },
  typescript: {
    strict: true,
    typeCheck: false,
    shim: false
  }
})