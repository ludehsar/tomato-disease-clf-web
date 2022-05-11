function uploadPhoto(event) {
  const [file] = event.target.files;
  
  const formData = new FormData();
  formData.append("file", file);

  if (file) {
      document.querySelector("#preview").src = URL.createObjectURL(file)
      URL.revokeObjectURL(file)
  } else {
      document.querySelector("#preview").src = "https://via.placeholder.com/300.png/09f/fff"
  }
}
