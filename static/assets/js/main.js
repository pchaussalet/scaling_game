var content = $('#content');

var launchApp = function() {
  content.addClass('container-fluid');
  $.getJSON('/product', renderProductList);
}

var renderProductList = function(productList) {
  var productIds = Object.keys(productList);
  var table = $('<table/>').addClass('table').addClass('table-striped');
  var thead = $('<thead/>');
  var header = $('<tr/>');
  header.append($('<td/>').append('ID'));
  header.append($('<td/>').append('Name'));
  header.append($('<td/>').append('Price'));
  header.append($('<td/>').append('Add to cart'));
  thead.append(header);
  table.append(thead);

  var tbody = $('<tbody/>');
  for (var i = 0; i < productIds.length; i++) {
    var productId = productIds[i];
    var product = productList[productId];
    var productLine = $('<tr/>');
    productLine.append($('<td/>').append(productId));
    productLine.append($('<td/>').append(product.name));
    productLine.append($('<td/>').append(product.price));
    productLine.append($('<td/>').append('+'));
    tbody.append(productLine);
  }
  table.append(tbody);
  $('#content').append(table);
}
