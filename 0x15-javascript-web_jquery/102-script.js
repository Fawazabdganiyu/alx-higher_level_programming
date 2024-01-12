$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const langCode = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      method: 'GET',
      data: { lang: langCode },
      success: (data) => {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
