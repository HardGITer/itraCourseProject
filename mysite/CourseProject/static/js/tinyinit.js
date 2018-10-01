tinymce.init({
  selector: '#editor',
  plugins: 'image code paste',
  toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignrigth alignjustify | bullist numlist outdent indent | link image media",
  // enable title field in the Image dialog
  image_title: true,
  image_upload_url: true,
  // enable automatic uploads of images represented by blob or data URIs
  automatic_uploads: true,
  // add custom filepicker only to Image dialog
  file_picker_types: 'image',
  paste_data_images:true,
  file_picker_callback: function(cb, value, meta) {
    var input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');

    input.onchange = function() {
      var file = this.files[0];
      var reader = new FileReader();

      reader.onload = function () {
        var id = 'blobid' + (new Date()).getTime();
        var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
        var base64 = reader.result.split(',')[1];
        //alert(base64);
        var blobInfo = blobCache.create(id, file, base64);
        //alert(blobInfo.blobUri());
        //blobInfo.blobUri() = "https://st.depositphotos.com/1752627/2306/i/450/depositphotos_23061294-stock-photo-hearts-drawn-on-the-sand.jpg";
        blobCache.add(blobInfo);
        // call the callback and populate the Title field with the file name
        cb(blobInfo.blobUri(), { title: file.name });
        //cb("https://st.depositphotos.com/1752627/2306/i/450/depositphotos_23061294-stock-photo-hearts-drawn-on-the-sand.jpg", { title: file.name });
        //alert(blobInfo.blobUri() + "  filename  " + file.name);
      };
      reader.readAsDataURL(file);
    };

    input.click();
  }
});