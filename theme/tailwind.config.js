module.exports = {
    content: [
      './core/templates/**/*.html',
      './posts/templates/**/*.html',
      './article/templates/**/*.html',
      './registration/templates/**/*.html',
      './franchise/templates/**/*.html',        // si tienes templates en theme/
    ],
    theme: {
      extend: {
        fontFamily: {
          barlow: ['Barlow', 'sans-serif'],
          osw: ['Oswald', 'sans-serif']
        },
      },
    },

    
    plugins: [],
  }
  