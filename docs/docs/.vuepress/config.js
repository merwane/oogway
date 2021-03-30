module.exports = {
    title: 'oogway',
    description: "A secure Bitcoin utility library for Python.",
    themeConfig:{
        nav: [
            { text: 'GitHub', link: 'https://github.com/merwane/oogway'}
        ],
        sidebar: [
            {
              title: 'Get started',
              collapsable: true,
              children: [
                  '/start/',
                  '/start/installation'
              ]
            },
            {
              title: 'Keys',
              collapsable: true,
              children: [
                  '/keys/',
                  '/keys/reference'
              ]
            },
            {
              title: 'Network',
              collapsable: true,
              children: [
                  '/network/',
                  '/network/reference'
              ]
            },
            {
              title: 'Node',
              collapsable: true,
              children: [
                  '/node/',
                  '/node/reference'
              ]
            },
            {
              title: 'Validation',
              collapsable: true,
              children: [
                  '/validation/',
                  '/validation/reference'
              ]
            },
            {
              title: 'Conversion',
              collapsable: true,
              children: [
                  '/conversion/',
                  '/conversion/reference'
              ]
            },
            {
              title: 'Operation',
              collapsable: true,
              children: [
                  '/operation/',
                  '/operation/reference'
              ]
            },
            {
              title: 'Transaction',
              collapsable: true,
              children: [
                  '/tx/',
                  '/tx/reference'
              ]
            },
            {
              title: 'Multisig',
              collapsable: true,
              children: [
                  '/multisig/',
                  '/multisig/reference'
              ]
            },
            {
              title: 'Fees',
              collapsable: true,
              children: [
                  '/fees/',
                  '/fees/reference'
              ]
            },
            {
              title: 'Payment requests',
              collapsable: true,
              children: [
                  '/payments/',
                  '/payments/reference'
              ]
            },
          ]
    },
    head: [
      ['link', { rel: 'icon', type: 'image/png', href: 'favicon-16x16.png', sizes: '16x16' }],
      ['link', { rel: 'icon', type: 'image/png', href: 'favicon-32x32.png', sizes: '32x32' }],
      ['link', { rel: 'apple-touch-icon', href: 'apple-touch-icon.png', sizes: '180x180' }],
      ['link', { rel: 'mask-icon', type: 'image/png', href: 'safari-pinned-tab.svg', color: '#ff9900' }],
      ['meta', { name: 'theme-color', content: '#ff9900' }],
      ['meta', { name: 'og:title', content: 'oogway' }],
      ['meta', { name: 'og:description', content: 'A secure Bitcoin utility library for Python.' }],
      ['meta', { name: 'og:url', content: 'https://oogway.merwanedrai.com' }],
      ['meta', { name: 'og:image', content: 'https://oogway.merwanedrai.com/meta_640.png' }],
      ['meta', { name: 'twitter:title', content: 'oogway' }],
      ['meta', { name: 'twitter:description', content: 'A secure Bitcoin utility library for Python.'}],
      ['meta', { name: 'twitter:card', content: 'summary' }],
      ['meta', { name: 'twitter:site', content: '@merwanedr' }],
      ['meta', { name: 'twitter:image', content: 'https://oogway.merwanedrai.com/meta_640.png' }],
      ['meta', { name: 'twitter:image:alt', content: 'Bitcoin logo' }],
      ['meta', { property: 'og:type', content: 'website' }]
    ]
}
