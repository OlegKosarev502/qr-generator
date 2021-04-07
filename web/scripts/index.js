function insertImage() {
  const image = document.createElement("img");
  image.setAttribute("src", "/img/result.png");

  const container = document.getElementById("container");
  container.appendChild(image);
}

function generate() {
  const url = document.getElementById("data").value;
  eel.generate_qr(url);

  setTimeout(insertImage, 1000);
}
