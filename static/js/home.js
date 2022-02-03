function overlay(isShow){
  var elm = document.getElementById('overlay')
  if (isShow) {
    elm.style.display = 'block';
  } else {
    elm.style.display = 'none';
  }
}

function openNav() {
  overlay(true);
  document.getElementById("sidenav").style.width = "88%";
}

function closeNav() {
  overlay(false);
  document.getElementById("sidenav").style.width = "0";
}
