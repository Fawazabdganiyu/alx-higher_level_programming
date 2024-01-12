$(document).ready(() => {
  function translate () {
    const langCode = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      method: 'GET',
      data: { lang: langCode },
      success: (data) => {
        $('DIV#hello').text(data.hello);
      }
    });
  }

  $('INPUT#btn_translate').on('click', translate);
  $('INPUT#language_code').on('keypress', (event) => {
    if (event.which === 13) {
      translate();
    }
  });
});
