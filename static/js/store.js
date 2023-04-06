var updateBtns = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;

    if (user === "AnonymousUser") {
      console.log("User is not authenticated");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  var url = "/update-item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((err) => console.log(err));
}
