const { description } = require('../../package')


module.exports = {
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: 'RPG GO Wiki',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,

  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }]
  ],

  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: true,
    nav: [
      {
        text: 'Guide',
        link: '/guide/',
      },
      {
        text: 'Collectables',
        link: '/collectables/'
      },
      {
        text: 'Events',
        link: '/events/'
      },
      {
        text: 'Play the game!',
        link: 'https://wngnelson.com/'
      }
    ],
  },

  sidebar: {
    '/guide/': [
      {
        title: 'Guide',
        collapsable: false,
        children: [
          '',
          'dungeon',
          'play'
        ]
      }
    ],
    '/collectables/': [
      {
        title: 'collectables',
        collapsable: false,
        children: [
          '',
          'where-to-find',
        ]
      }
    ],
    '/events/': [
      {
        title: 'events',
        collapsable: false,
      }
    ],
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
    '@vuepress/plugin-back-to-top',
    '@vuepress/plugin-medium-zoom',
  ]
}
