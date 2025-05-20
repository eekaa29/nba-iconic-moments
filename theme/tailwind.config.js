module.exports = {
    content: [
      '../core/templates/core/base.html',  // ajusta si tus templates están en otra app
      '../core/templates/core/home.html',
      '../core/templates/core/about.html',
      '../core/templates/core/contact.html',
      '../posts/templates/posts/post_list.html',
      '../posts/templates/posts/post_update_form.html',
      '../posts/templates/posts/create_form.html',
      '../posts/templates/posts/post_confirm_delete.html',
      '../article/templates/article/latest_articles.html',
      '../registration/templates/registration/login.html',
      '../registration/templates/registration/signup.html',
      '../registration/templates/registration/password_reset_form.html',
      '../registration/templates/registration/password_reset_done.html',
      '../registration/templates/registration/password_reset_confirm.html',
      '../registration/templates/registration/password_reset_complete.html',
      '../franchise/templates/franchise/franchise_list.html',        // si tienes templates en theme/
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }
  