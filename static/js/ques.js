function myFunction(answerId) {
  console.log('JavaScript is loaded');
  var x = document.getElementById(answerId);
  if (x.style.display === "block") {
      x.style.display = "none";
  } else {
      x.style.display = "block";
  }
}