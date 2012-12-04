
var launchApp = function() {
  $.ajaxSetup({contentType: 'application/json'});
  var catalog = $('<div id="catalog"/>').addClass('container-fluid');
  $.getJSON('/product', renderProductList);

  var cart = $('<div id="cart"/>').addClass('container-fluid');
  $.ajax('/cart', {type: 'PUT', success: function(data) {console.log(data); cart.val(data)}})
  
  var content = $('#content');
  content.addClass('container-fluid');
  content.append(catalog);
  content.append(cart);
}

var renderProductList = function(productList) {
  var productIds = Object.keys(productList);
  var table = $('<table/>').addClass('table').addClass('table-striped');
  var thead = $('<thead/>');
  var header = $('<tr/>');
  header.append($('<th/>').append('ID'));
  header.append($('<th/>').append('Name'));
  header.append($('<th/>').append('Price'));
  header.append($('<th/>').append('Add to cart'));
  thead.append(header);
  table.append(thead);

  var tbody = $('<tbody/>');
  for (var i = 0; i < productIds.length; i++) {
    var productId = productIds[i];
    var product = productList[productId];
    var productLine = $('<tr/>');
    var button = $('<a/>').addClass('btn');
    button.val('"'+product._id+'"');
    button.append(' + ');
    button.click(function() { addToCart(this); });
    productLine.append($('<td/>').append(productId));
    productLine.append($('<td/>').append(product.name));
    productLine.append($('<td/>').append(product.price));
    productLine.append($('<td/>').append(button));
    tbody.append(productLine);
  }
  table.append(tbody);
  $('#catalog').append(table);
}

var addToCart = function(button) {
  var productId = $(button).val();
  $.post('/cart/'+$('#cart').val(), String(productId), refreshCart, 'json');
}

var refreshCart = function(cartId) {
  $.getJSON('/cart/' + cartId + '?aggregated', renderCart);
  
}

var renderCart = function(cart) {
  var entries = cart.products;
  var productIds = Object.keys(entries);
  var table = $('<table/>').addClass('table').addClass('table-striped');
  var thead = $('<thead/>');
  var header = $('<tr/>');
  header.append($('<th/>').append('Name'));
  header.append($('<th/>').append('Price'));
  header.append($('<th/>').append('Count'));
  header.append($('<th/>').append('Total'));
  thead.append(header);
  table.append(thead);

  var tbody = $('<tbody/>');
  for (var i = 0; i < productIds.length; i++) {
    var productId = productIds[i];
    var product = entries[productId];
    var productLine = $('<tr/>');
    productLine.append($('<td/>').append(product.name));
    productLine.append($('<td/>').append(product.price));
    productLine.append($('<td/>').append(product.count));
    productLine.append($('<td/>').append(product.total));
    tbody.append(productLine);
  }
  table.append(tbody);
  var button = $('<a/>').addClass('btn').addClass('btn-primary').addClass('pull-right');
  button.append('Validate');
  button.click(generateInvoice);
  $('#cart').empty().append(table).append(button);
}

var generateInvoice = function() {
  var receipt = $('<div id="modal"/>').addClass('modal').addClass('fade').addClass('hide');
  var header = $('<div/>').addClass('modal-header');
  header.append($('<h3/>').append('Invoice'));
  var body = $('<div id="invoice"/>').addClass('modal-body');
  $.getJSON('/deal/'+$('#cart').val(), renderInvoice);
  receipt.append(header);
  receipt.append(body);
  $('#content').append(receipt);
}

var renderInvoice = function(cart) {
  var entries = cart.products;
  var productIds = Object.keys(entries);
  var table = $('<table/>').addClass('table').addClass('table-striped');
  var thead = $('<thead/>');
  var header = $('<tr/>');
  header.append($('<th/>').append('Name'));
  header.append($('<th/>').append('Price'));
  header.append($('<th/>').append('Count'));
  header.append($('<th/>').append('Total'));
  thead.append(header);
  table.append(thead);

  var tbody = $('<tbody/>');
  for (var i = 0; i < productIds.length; i++) {
    var productId = productIds[i];
    var product = entries[productId];
    var productLine = $('<tr/>');
    productLine.append($('<td/>').append(product.name));
    productLine.append($('<td/>').append(product.price));
    productLine.append($('<td/>').append(product.count));
    productLine.append($('<td/>').append(product.total));
    tbody.append(productLine);
  }

  var subLine = $('<tr/>');
  subLine.append($('<td/>').attr('colspan', '3').append('<strong>SubTotal</strong>'));
  subLine.append($('<td/>').append(cart.subtotal));
  tbody.append(subLine);

  var deals = Object.keys(cart.deals);
  for (var i = 0; i < deals.length; i++) {
    var dealName = deals[i];
    var dealRate = cart.deals[dealName];
    var dealLine = $('<tr/>');
    dealLine.append($('<td/>').attr('colspan', '2').append('<strong>Discount</strong> - ' + dealName));
    dealLine.append($('<td/>').attr('colspan', '2').css('text-align', 'center').append('-' + dealRate*100 + '%'));
    tbody.append(dealLine);
  }
  var discountLine = $('<tr/>');
  discountLine.append($('<td/>').attr('colspan', '3').append('<strong>Total discount</strong>'));
  discountLine.append($('<td/>').append(cart.discount));
  tbody.append(discountLine);
  var totalLine = $('<tr/>');
  totalLine.append($('<td/>').attr('colspan', '3').append('<strong>Total</strong>'));
  totalLine.append($('<td/>').append(cart.total));
  tbody.append(totalLine);

  table.append(tbody);
  $('#invoice').empty().append(table);
  
  $('#modal').modal();  
}

